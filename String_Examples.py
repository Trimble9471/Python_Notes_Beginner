#String concept examples
'''
#A string is a sequence of characters
#Note: In Python a character is treated as a string with 1 character

#Strings must be enclosed in matching single or double quotes
letter = 'A' #Same as if "A"
numChar = '4' #Same as "4"
message = "Good Morning" #Same as 'Good Morning'

x = '' #This is a empty string
y = "" #Also an empty string
print(type(x))
print(type(y))

#Note: Special kind of string denoted by triple quotes
#This preserves the tab and carriage returns

#print('''#There are three ways to represent strings:
    #1. Single-Quotes
    #2. Double-Quotes
    #3. Triple-Quotes.''')

#Import turtle
from turtle import *

#Display two chinese characters and 3 greek letters
#Unicode is an encoding scheme for international characters
write("\u6B22\u8FCE \u03b1 \u03b2 \u03b3", font=("Times",28))

#Unicode
#uniLetter = "\u0041"
#print(uniLetter)

#The ord and chr functions examples
#ord(ch) function for returning the ASCII code for the ch
#chr(code) function for returning the ch represented by the code

print(ord('a')) #WIll return the value of 97
print(chr(96)) #Will return the a
print(chr(ord('A')))
print(chr(ord('a') - ord('A')))

#Escape sequences for special characters
#Print a message with quotation marks in the output
#print("He said, "John's program is easy to read"")

#One way to fix is by using triple quotes
print('''He said,\n "John's program is easy to read."''')

#Other way, use escape sequences
print("\tHe said, \"John's program is easy to read.\"")

#Note: symbol \ and " together represent one character
#The backslash is called an escape character
#Common: \t, \n, \\, \", \', \r

#Printing without the newline
#print("AAA", end = '')
#print("BBB", end = ' ')
#print("CCC", end = '!!!!')
#print("DDD", end = '**\n')

#The String function
#can be used to return a string from any datatype
#s = str(4.7) #Returns a string from a floating point number
#print(type(s),s)

#s = str(True)
#print(str(s),s)

#The concatenation (+) and repetition (*) operators
#Join / concatenate two strings using +
#Can concatenate the same string multiple times with *
#s1 = "Welcome"
#s2 = "Python"
#s3 = s1 + " to " + s2
#print(s3)

#print("Welcome to Computer Science\n" * 5)

#Reading Strings from the console
#To read a string from the console use the input function
#first_name = input("Enter your first name: ")
#print("Student Name:", first_name + ' ' + last_name)
#print(f"Student Name: {first_name} {last_name}")

#The in and not in operators
#In and Not in is used to test whether a string is in another string
s1 = "Welcome"
print("Wel" in s1)
print("Wel" not in s1)

#s = input("Enter a string: ")

#if "Python" in s:
    #print("Python is in" ,s)
#else:
    #print("Python is not in" ,s)

#Comparing Strings
#Python compares strings by comparing their corresponding
#characters, and it does this by their numeric code (ASCII)
#We compare the first two characters then so on and so fourth
'''print("green" == "glow")
print("green" != "glow")
print("green" > "glow")
'''
#Functions for Strings
#len(), max(), min()

s = "Welcome"
print(len(s))

#Max and min functions return the largesst or smallest character
#Note: They do this using ASCII code value
print(max(s))
print(min(s))


#Index operator []
#A character in the string can be accessed through its index
#Indices are 0 based they range from 0 to len(s) - 1
s = "Welcome"
s1 = s[0]
print(s1)

#We can use negative numbers as indexes to reference
s2 = s[-2]
print(s2)

#WARNING: Strings are immutable objects. Their contents
#cannot change
#s[2] = 'A'

#Slicing operator [start index:ending index -1]
print(s[1:4])
print(s[ :5])
print(s[2: ])



