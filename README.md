# SwitchME
## Preamble ##
**This is NOT an Piracy device to circumvent anti-piracy mesures**  
**The SwitchME comes blank and YOU choose what to install on it**  

The SwitchMe is intended to have a more convient way to launch a payload on your device.
So you do not have to connect a usb cable to your computer and launch your payload.
There is no way to pirate anything with the SwithME.
**Again the SwitchME is not a circumvention device!**  

## Important informations ## 
* If you have Auto RCM enabled DISABLE, it until you flash the SwitchME for the first time (Use HekateCTCaer)
* If you flash any other payload other than Hekate CTCaer after enabling Auto RCM you will not have a way to flash
the SwitchME unless you can boot into Horizon  because there is no usb data comms while in RCM (for now)
* If you get stuck because of Auto RCM and only booting to say BISkeydump, the way around this is to disconnect either D+ or D- Boot into Horizon, reconnect the line and than flash the SwitchME bootloader
* Again this is only if you have Auto RCM enabled
* We highly suggest you only use Hekate CTCaer and put whatever payload you want to boot in the payloads directory of hekate.
* After Wiring in the SwitchME you can access the bootloader by conecting a USB-C cable directly to the switch. Make sure you have a compliant USB-C cable first though!
* A compliant cable will have a 56k Ohm resistor (check where you perchased your cable from). Really shouldnt be an issue if you are just flashing the SwitchMe directly from your computer, but be on the safe side as plenty of people have burned up their charge IC using 3rd party docks and cheap usb-c cables.

## Preflashing from a Computer ##
If you want to preflash the SwitchME connect a usb cable directly to the the board (D+ green) (D- white) (5v red) (gnd black)
On first connect to your computer it will already be in bootloader mode ready to be flashed.
After you have flashed the device for the very first time you will need to double press the button to go into bootloader mode again if you want to reflash the device, or if you connect the reset line you can do the same.
Also don't get confused. As soon as you successfully copied the *\*.uf2* file onto your SwitchMe device it will stop serving the disk and you don't have a change to successfully eject/umount it. It's the usual behaviour and everything should work as expected.

For Pre-Compiled payloads check UF2_SwitchME_Payloads

## Compile payloads on your own ##
To compile payloads for SwitchME you will need to install the Arduino IDE
https://www.arduino.cc/en/Main/Software
### Install the board manager for the SwitchME

1. Open Arduino IDE > Preferances > Additional Boards Manager URLs > Add The URL Below ```https://raw.githubusercontent.com/Aboshi/SwitchME/master/package_switchme_index.json```
1. Next go to *Tools > Board > Boards Manager > Type SAMD > Select Arduino SAMD Boards* and Install version 1.6.21
1. Next search for *rebug* and install it
1. You can now select *SwitchME m0* in the board programmer

### Compiling the payload ###
To compile different payoads you must first convert your payload.bin to hex
The easiest way is to use binConverter.py (you can find it in *Payload2UF2/main*).
Just use the following command line ```python2 binConverter.py </path/to/payload.bin>```. You need python2 for it.
A ```<payload>.h``` should be generated. 

Next open *SwitchME.ino* in *Payload2UF2/main* in the arduino application. 
Change *ctcaer\_4.0\_hekate.h* in the arduino sketchbook/project to whatever you named you payload. Make sure ```<payload>.h``` is in the same directory as the *SwitchMe.ino* file.
If you want to upload directly to your SwitchME just click on upload (your SwitchME is ready for use).
If you want to compile to make a .bin for converting to UF2 select *Sketch > Export compiled Binary*.

The final step is to convert the compiled *\*.bin* into the UF2 format. You can do this with *uf2conv.py* also located in *Payload2UF2/main*.
In this case you need python3. Here is the command line examle. ```python3 uf2conv.py -c main.ino.rebug_m0.bin```. Make sure the filename matches the generated *\*.bin*. A file named *flash.uf2* should be generated.

We try to keep all important payloads up to date. So in most cases you don't need to create your own *\*.uf2* files.

## Wiring Diagrams ##
Check the directory *wiring/4\_wire\_on\_at\_powerup* (when used with auto rcm you will get instant bootup to whatever you flahed the SwitchME with) We highly suggest CTCaer payloads!
More diagrams could be added soon with auto rcm line strapping, emmc cutoff (another auto rcm) and many others.
For now you can check this thread for other wiring methods that suit your needs:
https://gbatemp.net/threads/internal-modchip-samd21-trinket-m0-gemma-m0-itsybitsy-m0-express-guide-files-support.508068/

Huge thanks to @mattytrog for adding the SwitchMe to the current list!

## Generic Informations
The SwitchME also has 3.5mb of storage space. You can access it by putting the SwitchME into bootloader mode (double press the button).

## Credits ##
### Custom Firmware and Emulators ###

Create your own customized CFW and choose all included compontents:
https://www.sdsetup.com/
Thanks to @noahc3, @tomGER and all other contributers

Or Download an AIO package:
https://github.com/Team-Neptune/DeepSea/releases
Thanks to @Team-Neptune for keeping things up to date

Also have a look at this homebrew to automatically update all components (except the payload for the SwitchMe) automatically directly from the Switch.
https://github.com/HamletDuFromage/aio-switch-updater/releases

### Switch Scene ###
Greets to all the devs in the Switch scene without them none of this would be possible:
@SciresM @hexkyz @naewhert @oct0xor @ktemkin @CTCaer @rajkosto @Reisyukaku @atlas44 @noemu
@st4rk and countless others

### tools used ###
* [Euclala](https://github.com/euclala/) for the *binConverter.py*
* [Microsoft](https://github.com/microsoft/) for the *uf2conv.py*
