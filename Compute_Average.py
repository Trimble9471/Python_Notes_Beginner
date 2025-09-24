#Get 3 values from the user and find its average
'''
Step 1: Propt the user for three values
Step 2: Compute the average by adding all three values and divide by 3
Step 3: Display the results
'''

#Step 1
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

#Step 2
average = (num1 + num2 + num3) / 3

#Step 3
print(f"The average of {num1}, {num2}, {num3}, is {average}")

#Note: Python Interpreter cannot determine the end of a statement
#written in multiple lines.
#In this case yuou can line continuation symbol "\".
#Example:
'''
sum = 1 + 2 + 3 + 4 + 5 + \
      6 + 7 + 8 + 9 + 10

print(sum)
'''
