#Write a program to find out the Chinese Zodiac sign
#for a given year

'''
Note: The Chinese Zodiac sign is based on a 12 year cycle.
Each cycle represents a different animal
'''

#Promp the user to input a year
year = int(input("Enter a year: "))

#Compute the sign with formula
sign = year % 12

#Create multi-way if statement to find animal
if sign == 0:
    print("The year of the Monkey!")
elif sign == 1:
    print("The year of the Rooster!")
elif sign == 2:
    print("The year of the Dog!")
elif sign == 3:
    print("The year of the Pig!")
elif sign == 4:
    print("The year of the Rat!")
elif sign == 5:
    print("The year of the Ox!")
elif sign == 6:
    print("The year of the Tiger!")
elif sign == 7:
    print("The year of the Rabbit!")
elif sign == 8:
    print("The year of the Dragon!")
elif sign == 9:
    print("The year of the Snake!")
elif sign == 10:
    print("The year of the Horse!")
else:
    print("The year of the Sheep!")

#Nested Ex.
'''
if sign == 0:
    print()
else:
    if sign == 1:
        print()
    else:
        if sign == 2:
            print()
'''

