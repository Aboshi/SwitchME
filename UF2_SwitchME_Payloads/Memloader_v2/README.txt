memloader v2 (07.08.2018)
Parses ini files from microsd root and loads/decompresses/boots the appropriate binaries on the AArch64 CPU of the Nintendo Switch. 
Ini files can be generated from source images using the programs inside tools subdirectory. Currently the tools understand coreboot CBFS images or ELF payloads (like u-boot).

Usage
 Either put the appropriate ini+binary files onto your microsd card before inserting it into your Switch, or pass the --dataini parameter to TegraRcmSmash.exe to load them via USB.
 Send the memloader.bin to your Switch running in RCM mode via a fusee-launcher (sudo ./fusee-launcher.py memloader.bin or just drag and drop it onto TegraRcmSmash.exe on Windows)
 Follow the on-screen menu.


For updates check https://switchtools.sshnuke.net
Source code available at https://github.com/rajkosto/memloader

**I am not responsible for anything, including dead switches, loss of life, or total nuclear annihilation.**
