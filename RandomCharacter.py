#Description: Creating a random character module
#Note: ASCII Table will be a huge help

#Import the random module
from random import randint

#Generate a random character between ch1 and ch2
def getRandomCharacter(ch1,ch2):
    return chr(randint(ord(ch1),ord(ch2)))

#Generate a random lowercase letter
def getRandomLowerCaseLetter():
    return getRandomCharacter('a','z')

#Generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A','Z')

#Generate a random digit character
def getRandomDigitCharacter():
    return getRandomCharacter('0','9')

#Generate a random ascii character
def getRandomASCIICharacter():
    return getRandomCharacter(chr(32),chr(127))
