#Converting a hexadecimal digit to a decimal value
'''
Hexadecimal number system has 16 digits: 0-9 A-F
A = 10 (ASCII code 65)
B = 11 (ASCII code 66)
C = 12 (ASCII code 67)
D = 13 (ASCII code 68)
E = 14 (ASCII code 69)
F = 15 (ASCII code 70)
'''
#import the sys module
import sys

#Prompt the user to input a hecadecimal digit
hexDigit = input("Enter a hex digit: ").upper()

#Check if the hexDigit has exactly one character
if len(hexDigit) != 1:
    print("You must enter exactly one character")
    sys.exit()

#Display decimal value for hex digit
if hexDigit <= 'F' and hexDigit >= 'A':
    value = ord(hexDigit) - ord('A') + 10 #We add 10 because A = 10
    print(f"The decimal value for the hex digit {hexDigit} is {value}")
elif hexDigit.isdigit():
    print(f"The decimal value for hex digit {hexDigit} is {hexDigit}")
else:
    print(f"{hexDigit} is an invalid input")
    
