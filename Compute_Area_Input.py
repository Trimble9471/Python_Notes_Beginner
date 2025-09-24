#Computing the area of a circle with User input
'''
We can use the input() function to ask the user to input a value

Syntax = variable = input("Enter a value: ")

Note: The input function only reads input in as a String object!!!
Note: We can use the int(), float() to convert the string into a number
'''

#Prompt the user to input a value
radius = float(input("Enter a number for radius: "))

'''
string_object = input("message")
radius = float(string_object) Converts to a number
'''

#Compute the area
area = radius * radius * 3.14159

#Display the results
print("The area for the circle of radius", radius, "is", area)
