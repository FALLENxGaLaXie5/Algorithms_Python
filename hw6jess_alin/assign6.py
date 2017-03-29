# Group 10: Jessica Perez, Alinda Heng, and James Allen
# Assignment 6
# 12/01/2016

fileName = "cipher.txt"

byteSize = 8
cipher = ""
# Take binary input from file as string.
with open (fileName, "r") as myFile:
    for text in myFile:
        cipher = text

#print(cipher)

# Divide cipher into 8-bit characters.
cipherChar = [cipher[i: i + byteSize] for i in range(0, len(cipher), byteSize)]

outputFileName = "deciphered.txt"

# Will output file containing results.
outputFile = open(outputFileName, "w")

original = ""

# Range is from 0 to 256 because 255 is the largest 8-bit number (11111111).
# The range represents a possible key used to XOR the original text.
for key in range (0, 256):
    #print("Key:", key)
    outputFile.write("KEY: " + str(key) + "\n")
    outputFile.write("========\n")

    # Use XOR on each character.
    for character in cipherChar:
        originalChar = chr(int(character, 2) ^ key)
        original = original + originalChar

    # print(original)
    outputFile.write(original + "\n\n")
    original = ""

outputFile.close()

print("Finished deciphering message! Check", outputFileName, "for result!")
print("Note: The text is from Moby Dick, and the pad key is 110 (or 01101110 in binary). :)")