#Description: Counting the occurrence of each letter amongst 100 letters

#Import RandomCharacter module (CH6)
from RandomCharacter import *

#Create main
def main():
    #Create a list of characters
    #Invoke createList function
    chars = createList()

    #Display the list
    print("The lowercase letters are: ")

    #Invoke displayList function
    displayList(chars)

    #Count the occurrences of each letter
    counts = countLetters(chars)

    #Display the counts
    print("\nThe occurrences of each letter are:")
    displayCounts(counts)

#Create a list of characters
def createList():

    #Create a empty list
    chars = []

    #For loop to iterate 100x to append each letter for each iteration
    for i in range(100):
        chars.append(getRandomLowerCaseLetter())

    #Return the list
    return chars

#Create displayList
def displayList(chars):

    #Display the characters in the list 20 on each
    for i in range(len(chars)):
        if (i + 1) % 20 == 0:
            print(chars[i])
        else:
            print(chars[i], end = ' ')

#Create countLetters
def countLetters(chars):

    #Create a list of 26 integers with initial value of 0
    counts = 26 * [0]

    #For each lowercase letter in the list increment by 1 in its index
    for i in range(len(chars)):
        counts[ord(chars[i] - ord('a'))] += 1

    #Return the counts list
    return counts

#Display counts function
def displayCounts(counts):
    #Iterate through the indices
    for i in range(len(counts)):
        #Display 10 per line
        if (i + 1) % 10 == 0:
            print(counts[i], chr(i + ord('a')))
        else:
            print(counts[i], chr*i + ord('a'), end = ' | ')
            


main()
