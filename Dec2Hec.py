#Convert a base10 (decimal-integer) to a hexidecimal base16 representation
'''
This program repeatedly takes the remainder when dividing by 16 to
extract the rightmost hex digit, then moves left by using the integer division.
'''

#Prompt user to inter decimal integer
decimal = int(input("Enter a decimal integer: "))

#Create a variable to accumulate the hexadecimal digits in a string
hex = ""

#Continue looping as ong as there is still a positive value ot convert
while decimal != 0:
    #Capture the remainder
    hexValue = decimal % 16

    #Convert numeric digits (0-15) into the correct single hext char.
    if 0 <= hexValue <= 9:
        #Give the character for the digits
        hexChar = chr(hexValue + ord('0'))
    else:
        #For 10-15, but we want A-F
        #offset is 10
        hexChar = chr(hexValue - 10 + ord('A'))

    #Prepend the next hex digit to the left of our string
    hex = hexChar + hex

    #Integer divide by 16 to shift right 1 hex digit and keep converting
    decimal //= 16

#Once decimal reaches 0, display results
print(f"The hex number is {hex}")
