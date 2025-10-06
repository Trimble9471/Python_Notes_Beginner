#Reworking subtraction quiz to generate multiple questions
#Keep track of our correct answers

#Import random and time
import random, time

#Count the number of correct answers
correctCount = 0

#Count then number of questions
count = 0

#Max number of questions (CONSTANT)
NUM_OF_QUESTIONS = 5

#Start the timer
startTime = int(time.time())

#Create while loop to generate multiple questions
#a new question per iteration
while count < NUM_OF_QUESTIONS:

    #1. Generate two random single digit integers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    #2. If num1 is less than num2 swap
    if num1 < num2:
        num1,num2 = num2,num1

    #3. Prompt student to answer the question
    answer = int(input(f"What is {num1} - {num2}? "))

    #4. Grade the answer and display results
    if answer == num1 - num2:
        print("You are correct!")
        #Increment correct count
        correctCount += 1

    else:
        print(f"Your answer is wrong.\n" +
              f"{num1} - {num2} = {num1 - num2}")

    #5. Increment the count by 1
    count += 1

#Stop timer
stopTime = int(time.time())

#Compute the total time
testTime = stopTime - startTime

#Display the results
print(f"\nCorrect Count is {correctCount} / {NUM_OF_QUESTIONS}" +
      f"\nTest time is {testTime} seconds.")
