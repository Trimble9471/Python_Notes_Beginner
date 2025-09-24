#Develope a program for a 1st brader to practice subtraction

'''
Step 1: Generate two single digit integers
Step 2: if num1 < num2 swap values
Step 3: Prompt student to answer question
Step 4a: Check if answer is correct and display a message
Step 4b: Show a corrective message to the student
'''

#import random
from random import randint

#Step 1
num1 = randint(0,9)
num2 = randint(0,9)

#Step 2
if num1 < num2:
    num1, num2 = num2, num1
    #print("Swap Successful")

#Step 3
answer = int(input(f"What is {num1} - {num2}? "))

#Step 4
if num1 - num2 == answer:
    print("You are correct =)")

else:
    print("You are incorrect =(")
    print(f"Correct answer for {num1} - {num2} is {num1 - num2}")
    
    
