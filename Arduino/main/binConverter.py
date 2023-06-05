import sys
import binascii
import os


def printProgressBar(progress):
    i = int(progress * 20)
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()

def openFileToByte_generator(filename , chunkSize = 128):
    fileSize = os.stat(filename).st_size
    readBytes = 0.0
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunkSize)
            readBytes += chunkSize
            printProgressBar(readBytes/float(fileSize))
            if chunk:
                for byte in chunk:
                    yield byte
            else:
                break


if(len(sys.argv) is not 2):
	sys.exit('usage: binConverter.py "pathToFile\\fileName.bin"')

fileIn = sys.argv[1]


base = os.path.splitext(fileIn)[0]
fileOut =  base + ".h"

stringBuffer = "\t"
countBytes = 0
print("reading file: " + fileIn)

for byte in openFileToByte_generator(fileIn,16):
    countBytes += 1
    stringBuffer += "0x"+binascii.hexlify(byte).decode('ascii')+", "
    if countBytes%16 is 0:
    	stringBuffer += "\n\t"



stringBuffer = "#include <Arduino.h> \n \n#define FUSEE_BIN_SIZE " + str(countBytes) + "\nconst PROGMEM byte fuseeBin[FUSEE_BIN_SIZE] = {\n" + stringBuffer + "\n};"

print("\nwriting file: " + fileOut)
text_file = open(fileOut, "w")
text_file.write(stringBuffer)
text_file.close()

print("finished")