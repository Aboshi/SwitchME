biskeydump v6 (04.05.2018)
Dumps all your Switch BIS keys for eMMC contents decryption, to be used as a fusee payload.
With all your BIS keys and your RawNand.bin (or the physical eMMC attached via microSD reader or using a mass storage gadget mode in u-boot/linux) you can explore/modify your eMMC partitions using my HacDiskMount tool (if running Windows) from https://switchtools.sshnuke.net

Usage
 Send the biskeydump.bin to your Switch running in RCM mode via a fusee-launcher (sudo ./fusee-launcher.py biskeydump.bin or just drag and drop it onto TegraRcmSmash.exe on Windows)
 Either read out and note down the text printed on your Switch's screen, or scan the generated QR code with your phone to have a copy of all your device-specific keys
 Alternatively, use TegraRcmSmash 1.1.0 or newer with a dummy argument so it keeps listening for usb comms, and you will get all the keys inside the console window, sample cmdline:
    TegraRcmSmash.exe -w out/biskeydump.bin BOOT:0x0


For updates check https://switchtools.sshnuke.net
Source code available at https://github.com/rajkosto/biskeydump

**I am not responsible for anything, including dead switches, loss of life, or total nuclear annihilation.**
