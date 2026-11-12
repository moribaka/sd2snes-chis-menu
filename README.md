# 起司 SFC 菜单 / Chis SFC Menu

基于 sd2snes 原版菜单的中文适配与起司娘主题，提供固定语言菜单 ROM。

Chinese localization and the Chis theme for the original sd2snes menu, available as fixed-language menu ROMs.

| 样式 / Style | 中文 / Chinese | English |
| --- | --- | --- |
| 原版小字 / Original 8px | Original-8px-ZH.bin | Original-8px-EN.bin |
| 原版大字 / Original 12px | Original-12px-ZH.bin | Original-12px-EN.bin |
| 起司娘大字 / Chis 12px | Chis-12px-ZH.bin | Chis-12px-EN.bin |

每份 ROM 均为 3MiB，字体已经内置。英文版同样支持字库覆盖的中文文件名。
大字版使用同一套 CF12 字形：英文6×12、汉字12×12。

Each ROM is 3MiB and includes its fonts. English versions also display Chinese filenames covered by the font.
The large-font versions use CF12 glyphs: 6×12 for English and 12×12 for Chinese.

## 下载和使用 / Download and usage

请从 [Releases](https://github.com/moribaka/sd2snes-chis-menu/releases) 下载
sfc-menu-fixed-v0.1.1.zip。运行包只有六份菜单 ROM，没有外置字体、MCU 程序、FPGA 位流或游戏 ROM。

Download sfc-menu-fixed-v0.1.1.zip from [Releases](https://github.com/moribaka/sd2snes-chis-menu/releases).
It contains only the six menu ROMs. No external fonts, MCU firmware, FPGA bitstreams, or game ROMs are included.

先备份原菜单，再选择一个版本，按所用固件要求改成 m3nu.bin 或 menu.bin，
放回原来的菜单目录替换。其他固件、配置和存档文件不变。

Back up your existing menu, choose one version, and rename it to m3nu.bin or menu.bin as required by your firmware.
Replace the menu in its existing directory, leaving firmware, settings, and save files unchanged.

语言固定在 ROM 中，重启后不变，没有运行时语言选择，也不依赖固件保存语言。
需要固件支持原版 sd2snes 菜单协议、原版菜单地址布局及完整加载 3MiB 菜单镜像。

The language is fixed in each ROM and stays the same after restarting; there is no in-menu language selector.
Your firmware must support the original sd2snes menu protocol and memory layout, and load the full 3MiB menu image.

<a name="截图预览"></a>

## 截图预览 / Screenshots

| 版本 / Version | 主界面 / File browser | 设置菜单 / Settings |
| --- | --- | --- |
| 原版小字 · 中文<br>Original 8px · Chinese | <a href="images/screenshots/Original-8px-ZH-main.png"><img src="images/screenshots/Original-8px-ZH-main.png" alt="主界面 / File browser" width="320"></a> | <a href="images/screenshots/Original-8px-ZH-settings.png"><img src="images/screenshots/Original-8px-ZH-settings.png" alt="设置菜单 / Settings" width="320"></a> |
| 原版小字 · 英文<br>Original 8px · English | <a href="images/screenshots/Original-8px-EN-main.png"><img src="images/screenshots/Original-8px-EN-main.png" alt="主界面 / File browser" width="320"></a> | <a href="images/screenshots/Original-8px-EN-settings.png"><img src="images/screenshots/Original-8px-EN-settings.png" alt="设置菜单 / Settings" width="320"></a> |
| 原版大字 · 中文<br>Original 12px · Chinese | <a href="images/screenshots/Original-12px-ZH-main.png"><img src="images/screenshots/Original-12px-ZH-main.png" alt="主界面 / File browser" width="320"></a> | <a href="images/screenshots/Original-12px-ZH-settings.png"><img src="images/screenshots/Original-12px-ZH-settings.png" alt="设置菜单 / Settings" width="320"></a> |
| 原版大字 · 英文<br>Original 12px · English | <a href="images/screenshots/Original-12px-EN-main.png"><img src="images/screenshots/Original-12px-EN-main.png" alt="主界面 / File browser" width="320"></a> | <a href="images/screenshots/Original-12px-EN-settings.png"><img src="images/screenshots/Original-12px-EN-settings.png" alt="设置菜单 / Settings" width="320"></a> |
| 起司娘大字 · 中文<br>Chis 12px · Chinese | <a href="images/screenshots/Chis-12px-ZH-main.png"><img src="images/screenshots/Chis-12px-ZH-main.png" alt="主界面 / File browser" width="320"></a> | <a href="images/screenshots/Chis-12px-ZH-settings.png"><img src="images/screenshots/Chis-12px-ZH-settings.png" alt="设置菜单 / Settings" width="320"></a> |
| 起司娘大字 · 英文<br>Chis 12px · English | <a href="images/screenshots/Chis-12px-EN-main.png"><img src="images/screenshots/Chis-12px-EN-main.png" alt="主界面 / File browser" width="320"></a> | <a href="images/screenshots/Chis-12px-EN-settings.png"><img src="images/screenshots/Chis-12px-EN-settings.png" alt="设置菜单 / Settings" width="320"></a> |

## 源码 / Source code

菜单汇编源码位于 src，字库输入位于 fonts。

Menu assembly sources are in src, and font inputs are in fonts.

| 目录/文件 / Path | 内容 / Contents |
| --- | --- |
| roms | 六版 ROM / Six compiled menu ROMs |
| src/Original-* / src/Chis-* | 六版独立汇编项目 / Six standalone assembly projects |
| src/common | 共用菜单源码 / Shared menu sources |
| src/original_8px | 原版小字源码 / Original 8px sources |
| src/original_12px | 原版大字源码 / Original 12px sources |
| src/chis_12px | 起司娘大字源码 / Chis 12px sources |
| fonts | 字体输入及边框字形 / Font inputs and border glyphs |
| build.py | 菜单构建入口 / Menu build script |

Release 提供菜单ROM下载，源码可通过 GitHub 的 Source code 下载取得。
需要 Python 3.12 或更新版本，以及安装好的
[snescom / sneslink 1.8.1.1](https://bisqwit.iki.fi/src/arch/snescom-1.8.1.1.tar.gz)。

Menu ROMs are available in Releases; use GitHub's Source code download for the sources.
Building requires Python 3.12 or later and snescom / sneslink 1.8.1.1, linked above.

~~~text
python build.py
python build.py --variant original_12px --language en
~~~

Windows 下通过 WSL 调用工具；可用 --wsl-distro 指定发行版，
用 --snescom 和 --sneslink 指定工具路径。输出位于 build 目录。

On Windows, tools run through WSL. Use --wsl-distro to select a distribution, and
--snescom / --sneslink to specify tool paths. Output files are written to build.

源码修改说明：本次菜单适配与固定语言构建修改于2026-11-12。
src 中直接提供改版后的汇编源码，主要涉及中文绘字、主题排版及固定语言初始化。

Modification date: 2026-11-12. The assembly sources in src include Chinese text rendering,
theme layout changes, and fixed-language initialization.

## 鸣谢 / Acknowledgments

- [sd2snes 原工程](https://github.com/mrehkopf/sd2snes)及原作者、维护者和所有贡献者，提供菜单与功能基础。
  Thanks to the original sd2snes project, its authors, maintainers, and contributors for the menu and its underlying functionality.
- 特别感谢 **tiki**（西班牙菜单中文小字、大字作者）提供思路。
  Special thanks to tiki, author of the small- and large-font Chinese versions of the Spanish menu, for sharing ideas.
- [Fusion Pixel Font](https://github.com/TakWolf/fusion-pixel-font)及其上游字体作者，提供8px中文字体。
  Thanks to Fusion Pixel Font and its upstream font authors for the 8px Chinese font.
- 12px字形来自项目使用的 M+ HZK 12px 字库，保留原有 Copyright (c) 2020, op 署名。
  The 12px glyphs use the project's M+ HZK 12px font data, retaining its original copyright notice.

原版菜单参考 SD2SNES MENU v1.11.2，
对应提交为 [cf7e21d](https://github.com/mrehkopf/sd2snes/commit/cf7e21d7a5978fcd74981d71c3cfbf6e982a4dd1)。

Based on SD2SNES MENU v1.11.2 at the linked commit.

## 许可和署名 / License and attribution

菜单派生代码遵循原工程 GPLv2，完整文本见 LICENSE。
字体及其他第三方素材保留各自原有权利声明，见 LICENSES 和随附来源说明；
不以菜单代码许可改变字体许可。

The menu's derivative code follows the original project's GPLv2 license; see LICENSE.
Fonts and other third-party materials retain their own notices in LICENSES.
The menu code's license does not change the font licenses.
