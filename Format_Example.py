'''
Description: Formatting in Python

Option 1: format function (Built-in)
        syntax: format(item,format-specifier)

Option 2: format method (Str class)
        syntax: strObject.format()

Option 3: f-string (newest version)
        syntax: f or F in front of your string
                f"{item:format-specifier}"
F-strings are more concise and more efficient than the
format function
'''
#Import the math module
import math

#Display the header for each column
print(f"{'Degrees':10s}{'Radians':10s}{'Sine':7s}{'Cosine':9s}\
{'Tangent':10s}")

print('-' * 50)

#Display values for 30 degrees
degrees = 30
radians = math.radians(degrees)
print(f"{degrees:<10d}{radians:<10.4f}{math.sin(radians):<10.4f}\
{math.cos(radians):<10.4f}{math.tan(radians):<10.4f}")

#Display values for 60 degrees
degrees = 60
radians = math.radians(degrees)
print(f"{degrees:<10d}{radians:<10.4f}{math.sin(radians):<10.4f}\
{math.cos(radians):<10.4f}{math.tan(radians):<10.4f}")

#Display values for 90 degrees
degrees = 90
radians = math.radians(degrees)
print(f"{degrees:<10d}{radians:<10.4f}{math.sin(radians):<10.4f}\
{math.cos(radians):<10.4f}{math.tan(radians):<10.4f}")

#Format function
print(format(128,'10d'))
print(format(128,'10b'))
print(format(128,'10x'))
print(format(128,'10o'))
print(format(0.8874, '<5.1%'))

first_name = "John"
last_name = "Wick"
age = 22

print("First name: {1} \nLast name: {0} \nAge: {2:7b}".format(first_name,last_name,age))
