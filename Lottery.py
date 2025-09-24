#Develope a program to play a 2 digit lottery powerball
'''
Rule 1: If the user input matches the lottery in the exact
order we win $10,000

Rule 2: If the user input matches the lottery but in the wrong
order we win $3,000

Rule 3: If the user input matches 1 digit we win $1,000
'''
#Import random module
import random

#Generate a lottery number
lottery = random.randint(10,99)
#print(lottery)

#Prompt the user to input their guess
guess = int(input("Enter your lottery pick (2 digits): "))

#Get the digits from lottery
lDigit1 = lottery // 10 #Obtain 1st digit
lDigit2 = lottery % 10 #Obtains the last digit

#Get the digits from guess
gDigit1 = guess // 10
gDigit2 = guess % 10

#Display the winning lottery number
print(f"The Winning Lottery Number is {lottery}")

#Create a multi-way to check the rules for winning
if guess == lottery:
    print("Exact Match: You Win $10,000!")

elif gDigit2 == lDigit1 and gDigit1 == lDigit2:
    print("Match all Digits: You Win $3,000!")

elif (gDigit1 == lDigit1 or gDigit1 == lDigit2 or
      gDigit2 == lDigit1 or gDigit2 == lDigit2):
    print("Match One Digit: You Win $1,000!")

else:
    print("Sorry, Better luck next time")
