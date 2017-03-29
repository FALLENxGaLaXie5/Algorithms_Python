#Joshua Steward, Lowell Batacan
#Group 7
# Assignment 6
# 12/03/2016

file = "cipher.txt"

byteSize = 8
#cipher = ""
# This will grab the binary input and store it in a string to be parsed
with open(file, "r") as f:
    for text in f:
        #cipher = f.read().replace('\n', '')
        cipher = text
        print(cipher)

        # Divide cipher into 8-bit characters - still stored as strings, so it will convert to int.
        ciChar = [cipher[i: i + byteSize] for i in range(0, len(cipher), byteSize)]

        myOutput = "dec.txt"

        # Will output file containing results.
        outFile = open(myOutput, "w")

        # Range is from 0 to 256 because 255 is the largest 8-bit number (11111111).
        # The range represents a possible key used to XOR the original text.
        #will be used to display keys and to find possible decryption
        for key in range(0, 256):
            print("Key:", key)
            original = ""
            outFile.write("KEY: " + str(key) + "\n")
            outFile.write("========\n")

            # python XOR short on each int
            for character in ciChar:
                originalChar = chr(int(character, 2) ^ key)
                #originalChar = chr(ord('character') ^ key)
                #original = original + originalChar
                original += originalChar

            print(original)
            #outFile.write(original + "\n\n")

        outFile.close()
        print("The key is 110, and I do believe this is from Moby Dick! Deciphered text contained in " + myOutput)
