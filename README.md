# LumaLayeredFS Toolkit

English Manual: https://github.com/44670/layeredFS/wiki/manual

# 简介

LumaLayeredFS 是 LumaCFW 所使用的正版卡带(或 Titles)加载外置翻译数据的解决方案，只要将翻译数据安装至SD卡即可在正版卡带(或 Titles)运行时动态加载，达到正版卡(或 Titles)享受汉化游戏的目的。


# 工作原理

LumaLayeredFS 通过动态替换游戏的资源文件达到在不对正版卡带进行硬件上的修改的前提下修改部分语言文件的目的。当游戏请求访问资源文件时，将检测SD卡上的翻译数据目录下是否有同名的翻译文件，如果有则进行重定向（如果没有的话仍然访问原始的文件）。只要提供包含修改过的资源文件的翻译数据，即可实现汉化。


# 使用方法

需要安装下列软件:  
python 3.x: https://www.python.org/

 1. 将解密后的 exefs.bin 和 exh.bin 放入 workdir 目录，将原版的 romfs 文件夹命名为 romfs1 或 romfs.bin 文件重命名为 romfs1.bin ，翻译后的 romfs 文件夹重命名为 romfs2 或 romfs.bin 重命名为 romfs2.bin ，放入 workdir 目录。
 2. 运行 build_layeredfs.bat。
 3. 将在 workdir 里生成的 luma 目录，拷贝到 SD 卡。
 4. 运行正版游戏后，将自动应用翻译数据，重定向文件。


# 已知问题

部分游戏由于未知的原因无法运行。（已修复）
