# SwitchME

_________________________________________________________________________________________

* For Pre-Compiled payloads check the releases ection *

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

You can find all the tools you need in the Release section of this Git
We will provide plenty of payloads in UF2 format and keep them updated when updates are released.

Greets to all the dev in the Switch scene without them none of this would be possible:
@SciresM @hexkyz @naewhert @ktemkin @CTCaer @rajkosto @Reisyukaku @atlas44 @noemu
@st4rk and countless others
