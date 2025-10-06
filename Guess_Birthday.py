#Converting a binary to its integer form and finding
#the day you were born on

#Birthday to be determined
day = 0

#Prompt the user to answer the first question
question1 = "Is your birthday in Set1?\n" +\
            " 1  3  5  7\n" + \
            " 9 11 13 15\n" + \
            "17 19 21 23\n" + \
            "25 27 29 31\n" + \
            "Enter n/N for No and y/Y for Yes: "
answer = input(question1)

#One way if statement to check for the Y response
if answer.upper() == 'Y':
    #Bit 1
    day += 1

#Prompt the user to answer the second question
question2 = "Is your birthday in Set2?\n" +\
            " 2  3  6  7\n" + \
            "10 11 14 15\n" + \
            "18 19 22 23\n" + \
            "26 27 30 31\n" + \
            "Enter n/N for No and y/Y for Yes: "
answer = input(question2)

#One way if statement to check for the Y response
if answer.upper() == 'Y':
    #Bit 2
    day += 2

#Prompt the user to answer the third question
question3 = "Is your birthday in Set3?\n" +\
            " 4  5  6  7\n" + \
            "12 13 14 15\n" + \
            "20 21 22 23\n" + \
            "28 29 30 31\n" + \
            "Enter n/N for No and y/Y for Yes: "
answer = input(question3)

#One way if statement to check for the Y response
if answer.upper() == 'Y':
    #Bit 3
    day += 4

#Prompt the user to answer the third question
question4 = "Is your birthday in Set4?\n" +\
            " 8  9 10 11\n" + \
            "12 13 14 15\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31\n" + \
            "Enter n/N for No and y/Y for Yes: "
answer = input(question4)

#One way if statement to check for the Y response
if answer.upper() == 'Y':
    #Bit 4
    day += 8

#Prompt the user to answer the third question
question5 = "Is your birthday in Set5?\n" +\
            "16 17 18 19\n" + \
            "20 21 22 23\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31\n" + \
            "Enter n/N for No and y/Y for Yes: "
answer = input(question5)

#One way if statement to check for the Y response
if answer.upper() == 'Y':
    #Bit 5
    day += 16

#Display results
print(f"\nYour Birthday is {day}!")

#n | n | n | y | n
#0 | 0 | 0 | 1 | 0
