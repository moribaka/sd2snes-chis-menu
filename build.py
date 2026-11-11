"""只编译菜单源码；依赖外部snescom/sneslink，不携带工具链。"""
from pathlib import Path
import argparse,hashlib,os,re,shutil,struct,subprocess
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parent

def font8():
    path=ROOT/'fonts/fusion-pixel-8px-monospaced-zh_hans.bdf'
    text=path.read_text('utf-8');glyphs={}
    for item in text.split('STARTCHAR ')[1:]:
        code=int(re.search(r'(?m)^ENCODING (\d+)$',item)[1])
        w,h,x,y=map(int,re.search(r'(?m)^BBX (-?\d+) (-?\d+) (-?\d+) (-?\d+)$',item).groups())
        if code>65535 or w>8 or h>8:continue
        rows=item.split('BITMAP\n',1)[1].split('ENDCHAR',1)[0].strip().splitlines();bits=[0]*8
        for row,hexrow in enumerate(rows):
            yy=7-y-h+row
            if not 0<=yy<8:continue
            value=int(hexrow,16);storage=((w+7)//8)*8
            for column in range(w):
                xx=x+column
                if 0<=xx<8 and value&(1<<(storage-1-column)):bits[yy]|=1<<(7-xx)
        glyphs[code]=bytes(bits)
    fallback=glyphs[0x25a1];data=bytearray()
    for code in range(65536):
        for row in glyphs.get(code,fallback):
            expanded=sum(3<<(14-2*x) for x in range(8) if row&(0x80>>x))
            data+=struct.pack('>H',expanded)
    return bytes(data),glyphs

def font12():
    pack=(ROOT/'fonts/menu_font12.pack').read_bytes()
    records={int.from_bytes(pack[i:i+4],'little'):(pack[i+4:i+8],pack[i+8:i+32])
             for i in range(530,len(pack),32)}
    codes=sorted(records);slots={cp:n for n,cp in enumerate(codes)}
    data=bytearray(0x100000);fallback=slots[0x25a1]
    for cp in range(65536):
        pointer=0xe30000+72*slots.get(cp,fallback)
        for lane in range(3):data[lane*65536+cp]=(pointer>>(lane*8))&255
        data[0xf0000+cp]=12
    for cp,n in slots.items():
        metadata,bits=records[cp]
        width=int.from_bytes(metadata,'little')
        assert width in (4,6,12),(cp,width)
        if cp==32:width=6
        data[0xf0000+cp]=width
        for yy in range(12):
            value=int.from_bytes(bits[yy*2:yy*2+2],'big')>>4
            for segment in range(6):
                pair=(value>>(10-2*segment))&3
                data[0x30000+n*72+yy*6+segment]=(12 if pair&2 else 0)|(3 if pair&1 else 0)
    assert 0x30000+len(codes)*72<=0xec000
    text=(ROOT/'src/original_8px/font.a65').read_text('utf-8')
    lines='\n'.join(line.split(';')[0] for line in text.splitlines() if '.byt' in line)
    font=bytes(int(v,16) for v in re.findall(r'\$([0-9a-fA-F]{2})(?![0-9a-fA-F])',lines))
    assert len(font)==4096
    frames=(ROOT/'fonts/frame12.a65').read_text('utf-8').split('zh12_frame:')[1].split('#define')[0]
    frame_rows=[]
    for line in frames.splitlines():
        if '.byt' in line:
            frame_rows.append([int(v.strip().replace('$','0x'),0) for v in line.split('.byt')[1].split(';')[0].split(',')][:12])
    assert len(frame_rows)==10
    for cp in range(256):
        for yy in range(12):
            value=frame_rows[cp-20][yy] if 20<=cp<30 else (font[cp*16+(yy-2)*2] if 2<=yy<10 else 0)
            if cp in (31,32):value=0
            data[0xec000+cp*24+yy*2:0xec000+cp*24+yy*2+2]=bytes((value>>4,value&15))
    for y in range(216):
        row=y//8
        offset=(0x8000+(row//2)*1024 if row&1 else (row//2)*2048)+(y&7)*2
        struct.pack_into('<H',data,0xef000+y*2,offset)
    assert all(data[0xf0000+cp]==6 for cp in range(32,127))
    return bytes(data),{cp:bits for cp,(_,bits) in records.items()}

def linux(path):
    path=Path(path).resolve()
    return '/mnt/'+path.drive[0].lower()+path.as_posix()[2:] if path.drive else str(path)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--variant',choices=['original_8px','original_12px','chis_12px'])
    parser.add_argument('--language',choices=['zh','en'])
    parser.add_argument('--snescom',default='snescom')
    parser.add_argument('--sneslink',default='sneslink')
    parser.add_argument('--wsl-distro')
    args=parser.parse_args()
    def command(executable,arguments,project,log):
        if os.name=='nt':
            executable=linux(executable) if Path(executable).drive else executable
            cmd=['wsl',*(['-d',args.wsl_distro] if args.wsl_distro else []),
                 '--cd',linux(project),'--',executable,*arguments]
            cwd=None
        else:cmd=[executable,*arguments];cwd=project
        result=subprocess.run(cmd,cwd=cwd,capture_output=True)
        log.write_bytes(result.stdout+result.stderr)
        if result.returncode or re.search(rb'(?m)^Error:',result.stdout+result.stderr):
            raise RuntimeError(log.read_text('utf-8',errors='replace'))
    names='header reset main font palette data const logo logospr dma filesel pad time sysinfo spc700 spcplay menu menudata ui nmihook common savestate near zh_engine'.split()
    for variant in ([args.variant] if args.variant else ['original_8px','original_12px','chis_12px']):
        glyphs=font8()[0] if variant=='original_8px' else font12()[0]
        assert len(glyphs)==0x100000
        for language in ([args.language] if args.language else ['zh','en']):
            project=ROOT/'build'/(variant+'_'+language)/'project'
            project.mkdir(parents=True,exist_ok=True)
            for folder in (ROOT/'src/common',ROOT/'src'/variant):
                for file in folder.iterdir():
                    if file.suffix in ('.a65','.i65'):shutil.copyfile(file,project/file.name)
            (project/'language.i65').write_text('#define FIXED_LANGUAGE '+str(int(language=='en'))+'\n','utf-8')
            modules=names+([] if variant=='original_8px' else ['theme'])
            def assemble(name):
                fixed=name in ('header','nmihook','common','savestate')
                target=name+('.ips' if fixed else '.o65')
                command(args.snescom,[*(['-I'] if fixed else []),'-J','-Wall','-o',target,name+'.a65'],
                        project,project/(name+'.log'))
                return target
            with ThreadPoolExecutor(max_workers=2) as pool:objects=list(pool.map(assemble,modules))
            command(args.sneslink,['-fsmc','-o','menu_code.bin',*objects],project,project/'link.log')
            code=(project/'menu_code.bin').read_bytes();assert len(code)==65536
            rom=bytearray(0x300000);rom[:65536]=code;rom[0x200000:]=glyphs
            rom[0xffd7]=0x0c;rom[0xffdc:0xffe0]=b'\xff\xff\0\0'
            total=(sum(rom[:0x200000])+2*sum(rom[0x200000:]))&65535
            struct.pack_into('<HH',rom,0xffdc,total^65535,total)
            prefix={'original_8px':'Original-8px','original_12px':'Original-12px','chis_12px':'Chis-12px'}[variant]
            target=ROOT/'build'/(prefix+'-'+language.upper()+'.bin');target.write_bytes(rom)
            print(target.name,hashlib.sha256(rom).hexdigest(),flush=True)

if __name__=='__main__':main()
