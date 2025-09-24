#Develope a program to help a 1st grader with addition

'''
Step 1: Generate two singel-digit integers
Step 2: Prompt the student to answer the question
Step 3: Display: check student answer is correct
'''

#Import the random module
import random

#Step 1
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

#Step 2
answer = int(input(f"What is {number1} + {number2}? "))

#Step 3
print(f"{number1} + {number2} = {answer}")
print(f"The result is {number1 + number2 == answer}")

