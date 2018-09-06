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

* For Pre-Compiled payloads check the releases section *

_________________________________________________________________________________________

To compile payloads for SwitchME you wil need to install the Arduino IDE
https://www.arduino.cc/en/Main/Software

~ Next you must install the board manager for SwitchME ~

Open Arduino IDE > Preferances > Additional Boards Manager URLs > Add The URL Below
https://raw.githubusercontent.com/Aboshi/SwitchME/master/package_switchme_index.json

Next go to Tools > Board > Boards Manager
Type SAMD > Select Arduino SAMD Boards and Install

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

Greets to all the dev in the Switch scene without them none of this would be possible:
@SciresM @hexkyz @naewhert @oct0xor @ktemkin @CTCaer @rajkosto @Reisyukaku @atlas44 @noemu
@st4rk and countless others
