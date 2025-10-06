#Reworking the subtraction quiz to take answers
#until the student answers correctly

#Import random module
from random import randint

#1. Generate two random single digit integers
num1 = randint(0,9)
num2 = randint(0,9)

#2. Swap values if num1 is smaller than num2
if num1 < num2:
    num1,num2 = num2,num1

#3. Promp the student to answer the question?
answer = int(input(f"What is {num1} - {num2}? "))

#Create a while loop to check answers
#Reprompt the student until they anser correctly
while num1 - num2 != answer:
    answer = int(input(f"Wrong Answer. Try again!" +
                       f"What is {num1} - {num2}? "))
#Display a message to the student
print("Correct!")
