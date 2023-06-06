
# Rebug SwitchME Wiki
Welcome to the official Rebug SwitchME Repository. Here you can find all documentation related to the SwitchME, creating payloads, installing the chip and more. All suggestions & contributions are massively appreciated!


## Firmware & Payloads
For Pre-Compiled Modchip UF2 Payloads check [/UF2_SwitchME_Payloads](https://github.com/Aboshi/SwitchME/tree/master/UF2_SwitchME_Payloads)

## Converting a payload.bin to UF2

### Requirements: 
- [Arduino IDE](https://www.arduino.cc/en/Main/Software)

### Requirements Steps:

 1. Open Arduino IDE > Preferances > Additional Boards Manager URLs > Add The URL Below
https://raw.githubusercontent.com/Aboshi/SwitchME/master/package_switchme_index.json

2. Go to Tools > Board > Boards Manager > Type SAMD > Select Arduino SAMD Boards and Install version 1.6.21

3. Search for Rebug and install Rebug Samd Boards 1.0.4

4. Close Board Manager. 

5. Select Rebug from Boards Dropdown.

6. Refer to [this File](https://github.com/Aboshi/SwitchME/blob/master/Arduino/main/How%20to%20use.txt) for instructions on how to compile.

You can find all the tools you need in the releases section of this git as well as pre compiled payloads in UF2 format
We will provide plenty of payloads in UF2 format and keep them updated with new releases.

## Wiring Diagrams:

[Method 1](https://github.com/Aboshi/SwitchME/tree/master/wiring/4_wire_on_at_powerup): (when used with auto rcm you will get instant bootup to whatever you flahed the SwitchME with) We highly suggest CTCaer payloads!
- More diagrams will be added soon with auto rcm line strapping, emmc cutoff (another auto rcm) and many others.

For now you can check this thread for other wiring methods that suit your needs:
https://gbatemp.net/threads/internal-modchip-samd21-trinket-m0-gemma-m0-itsybitsy-m0-express-guide-files-support.508068/

Huge thanks to @mattytrog for adding the SwitchMe to the current list!
## Important Notes:

- Make sure you have a compliant USB-C cable! A compliant cable will have a 56k Ohm resistor.

- The SwitchME also has 3.5mb of storage space. You can access it by putting the SwitchME into bootloader mode (double press the button)

- If you want to preflash the SwitchME connect a USB cable directly to the the board (D+ green) (D- white) (5v red) (gnd black).

- On first connect to your computer it will already be in bootloader mode ready to be flashed.

 - If you are flashing your chip for the first time and have Auto RCM enabled, DISABLE until the chip is flashed. (Use CTCaer 6.0.4+) to re-enable AutoRCM.
 
 - If you flash any other payload other than Hekate CTCaer after enabling Auto RCM you will not have a way to flash the SwitchME again until you can boot into Nintendo OS (HOS) because the USB port will not work while in RCM.

- If you get stuck because of Auto RCM and only booting to a payload that isn't Hekate CTCaer, the way around this is to disconnect either D+ or D- Boot into Nintendo OS (HOS), reconnect the line and than flash the SwitchME bootloader.

- We highly suggest you only use Hekate CTCaer and put all your other payloads in `bootloader/payloads` on your SD card. This way when you turn on your switch and boot into Hekate, you can choose Payloads and boot into whatever one you want.

## Bootloader Mode:
Bootloader mod is a mode you can put the modchip into which allows you to copy a new uf2 file (payload).
You can access this mode by plugging your switch into a PC using a USB-C Cable, then booting into Horizon, then double tapping the modchip button. A new drive will popup which will accept a new uf2 file.


## Useful Links & Resources:
Custom Firmware and Emulators:

https://www.sdsetup.com/
Thanks to @noahc3 & @tomGER

AIO Package:
https://github.com/tumGER/SDFilesSwitch/releases
Thanks to @tomGER for keeping things up to date
_________________________________________________________________________________________

Greets to all the devs in the Switch scene without them none of this would be possible:
@SciresM @hexkyz @naewhert @oct0xor @ktemkin @CTCaer @rajkosto @Reisyukaku @atlas44 @noemu
@st4rk and countless others
