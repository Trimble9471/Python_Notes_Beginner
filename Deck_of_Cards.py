#Description: Pick four random cards out of a 52 Card deck

#Import random module
from random import shuffle

#Create a deck of cards
deck = [x for x in range(0,51)]

#Create suites and ranks lists
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", '2', '3', '4', '5', '6', '7', '8', '9',
         '10', "Jack", "Queen", "King"]

#Shuffle the cards
shuffle(deck)

#Create a for loop to iterate 4 times to display our random cards
for i in range(4):
    #Suit calculation: since there are 13 cards in each suit,
    #deck = 0-12 the result will be 0
    #deck = 12-25 the results will be 1
    suit = suits[deck[i] // 13]

    #Rank calculation: the module operation gives the remainder when
    #the card index is divided by 13, mapping the card index to its rank
    rank = ranks[deck[i] % 13]

    #Display the card
    print(f"Card Number: {deck[i]} is {rank} of {suit}")
