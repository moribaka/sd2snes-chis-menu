# 起司 SFC 菜单

基于 sd2snes 原版菜单的中文适配与起司娘主题，提供固定语言菜单 ROM。

| 样式 | 中文 | English |
| --- | --- | --- |
| 原版小字 8px | Original-8px-ZH.bin | Original-8px-EN.bin |
| 原版大字 12px | Original-12px-ZH.bin | Original-12px-EN.bin |
| 起司娘大字 12px | Chis-12px-ZH.bin | Chis-12px-EN.bin |

每份 ROM 均为 3MiB，字体已经内置。英文版同样支持字库覆盖的中文文件名。
大字版使用同一套 CF12 字形：英文6×12、汉字12×12。

## 下载和使用

请从 [Releases](https://github.com/moribaka/sd2snes-chis-menu/releases) 下载
sfc-menu-fixed-v0.1.0.zip。运行包只有六份菜单 ROM，没有外置字体、MCU 程序、FPGA 位流或游戏 ROM。

先备份原菜单，再选择一个版本，按所用固件要求改成 m3nu.bin 或 menu.bin，
放回原来的菜单目录替换。其他固件、配置和存档文件不变。

语言固定在 ROM 中，重启后不变，没有运行时语言选择，也不依赖固件保存语言。
需要固件支持原版 sd2snes 菜单协议、原版菜单地址布局及完整加载 3MiB 菜单镜像。

## 源码

菜单汇编源码位于 src，字库输入位于 fonts。

| 目录/文件 | 内容 |
| --- | --- |
| src/common | 三种样式共用的菜单源码 |
| src/original_8px | 原版小字源码 |
| src/original_12px | 原版大字源码 |
| src/chis_12px | 起司娘大字源码 |
| fonts | 对应的原始字体输入及边框字形 |
| build.py | 构建入口，生成菜单ROM |

Release 提供菜单ROM下载，源码可通过 GitHub 的 Source code 下载取得。
需要 Python 3.12 或更新版本，以及安装好的
[snescom / sneslink 1.8.1.1](https://bisqwit.iki.fi/src/arch/snescom-1.8.1.1.tar.gz)。

~~~text
python build.py
python build.py --variant original_12px --language en
~~~

Windows 下通过 WSL 调用工具；可用 --wsl-distro 指定发行版，
用 --snescom 和 --sneslink 指定工具路径。输出位于 build 目录。

源码修改说明：本次菜单适配与固定语言构建修改于2026-11-11。
src 中直接提供改版后的汇编源码，主要涉及中文绘字、主题排版及固定语言初始化。

## 鸣谢

- [sd2snes 原工程](https://github.com/mrehkopf/sd2snes)及原作者、维护者和所有贡献者，提供菜单与功能基础。
- 特别感谢 **tiki**（西班牙菜单中文小字、大字作者）提供思路。
- [Fusion Pixel Font](https://github.com/TakWolf/fusion-pixel-font)及其上游字体作者，提供8px中文字体。
- 12px字形来自项目使用的 M+ HZK 12px 字库，保留原有 Copyright (c) 2020, op 署名。

原版菜单参考 SD2SNES MENU v1.11.2，
对应提交为 [cf7e21d](https://github.com/mrehkopf/sd2snes/commit/cf7e21d7a5978fcd74981d71c3cfbf6e982a4dd1)。

## 许可和署名

菜单派生代码遵循原工程 GPLv2，完整文本见 LICENSE。
字体及其他第三方素材保留各自原有权利声明，见 LICENSES 和随附来源说明；
不以菜单代码许可改变字体许可。
