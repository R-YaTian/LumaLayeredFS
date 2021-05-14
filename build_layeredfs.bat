set PATH=%PATH%;C:\devkitPro\devkitARM\bin

del plugin\source\autogen.h

ctrtool --decompresscode -t exefs --exefsdir=workdir\exefs workdir\exefs.bin

locate.py workdir\exefs\code.bin

pause
