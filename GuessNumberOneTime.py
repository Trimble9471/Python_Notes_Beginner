#Randomly generating a number to be guessed

#Import random
from random import randint

#Generate a random number 0-100
number = randint(0,100)
print(number)

#Display a statement
print("Guess a magic number between 0 and 100")

#Prompt the user to guess their number
guess = int(input("Enter your guess: "))

#Multi-way to check the guess
if guess == number:
    print("Yes, the number is is {guess}")
elif guess > number:
    print("Your guess is too high!")
elif guess < number:
    print("Your guess is too low!")


