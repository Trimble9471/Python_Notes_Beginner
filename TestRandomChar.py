#Description: testing the functions in the custom module

from RandomCharacter import *

#Number of characters to generate
NUM_OF_CHARS = 100

#Number of characters to display per line
CHARS_PER_LINE = 20

#Print random lowercase characters
for i in range(NUM_OF_CHARS):
    #Display the Lowercase letter
    print(getRandomLowerCaseLetter(), end = '')

    #Check if we have 20 on the line
    if (i + 1) % CHARS_PER_LINE == 0:
        print() #Jump to next line

print()

#Print random uppercase characters
for i in range(NUM_OF_CHARS):
    #Display the Uppercase letter
    print(getRandomUpperCaseLetter(), end = '')

    #Check if we have 20 on the line
    if (i + 1) % CHARS_PER_LINE == 0:
        print() #Jump to next line

print()

#Print random random digit characters
for i in range(NUM_OF_CHARS):
    #Display the random digit
    print(getRandomDigitCharacter(), end = '')

    #Check if we have 20 on the line
    if (i + 1) % CHARS_PER_LINE == 0:
        print() #Jump to next line

print()
