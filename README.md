# SwitchME

_________________________________________________________________________________________

After Wiring in the SwitchME you can access the bootloader by conecting a usb-c cable directly to the switch.
Make sure you have a compliant ucb-c cable first though!
A compliant cable will have a 56k Ohm resistor (check where you perchased your cable from)
Really shouldnt be an issue if you are just flashing the SwitchMe directly from your computer, but be on the safe side as plenty of people have burned up their charge IC using 3rd party docks and cheap usb-c cables.

If you want to preflash the SwitchME connect a usb cable directly to the the board (D+ green) (D- white) (5v red) (gnd black)
On first connect to your computer it will already be in bootloader mode ready to be flashed.
After you have flashed the device for the very first time you will need to double press the button to go into bootloader mode again if you want to reflash the device, or if you connect the reset line you can do the same.

_________________________________________________________________________________________

For Pre-Compiled payloads check UF2_SwitchME_Payloads

_________________________________________________________________________________________

To compile payloads for SwitchME you will need to install the Arduino IDE
https://www.arduino.cc/en/Main/Software

~ Next you must install the board manager for SwitchME ~

Open Arduino IDE > Preferances > Additional Boards Manager URLs > Add The URL Below
https://raw.githubusercontent.com/Aboshi/SwitchME/master/package_switchme_index.json

Next go to Tools > Board > Boards Manager > Type SAMD > Select Arduino SAMD Boards and Install

Next search for rebug and install

You can now select SwitchME m0 in the board programmer

_________________________________________________________________________________________

To compile different payoads you must first conver your payload.bin to hex
The easiest way is to use binConverter.py (you can find it under releases)
Open SwitchME.ino
Change ctcaer_4.0_hekate.h to whatever you named you payload
If you want to upload directly to your SwitchME just click on upload (your SwitchME is ready for use)
If you want to compile to make a .bin for converting to UF2 select Sketch > Export compiled Binary

You can find all the tools you need in the releases section of this git as well as pre compiled payloads in UF2 format
We will provide plenty of payloads in UF2 format and keep them updated when updates are released.

_________________________________________________________________________________________

Wiring Diagrams:
Simple 4 wire always on diagram is in the wiring dir
More diagrams will be added soon with auto rcm line strapping, voltage dropout method, emmc cutoff (another auto rcm) and many others.

You can also find complete wiring diagrams below:
https://gbatemp.net/threads/internal-modchip-samd21-trinket-m0-gemma-m0-itsybitsy-m0-express-guide-files-support.508068/

Huge thanks to @mattytrog for adding the SwitchMe to the current list!
_________________________________________________________________________________________

Custom Firmware and Emulators:

Roll your own:
https://www.sdsetup.com/
^^
Thanks to @noahc3 & @tomGER

Or Download an AIO package:
https://github.com/tumGER/SDFilesSwitch/releases
^^ Tkanks to @tomGER for keeping things up to date
_________________________________________________________________________________________

The SwitchME also has 3.5mb of storage space. You can access it by putting the SwitchME into bootloader mode (double press the button)

Greets to all the devs in the Switch scene without them none of this would be possible:
@SciresM @hexkyz @naewhert @oct0xor @ktemkin @CTCaer @rajkosto @Reisyukaku @atlas44 @noemu
@st4rk and countless others
