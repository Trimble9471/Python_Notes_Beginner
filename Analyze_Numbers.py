#Find all the values above the average
#Extra content
from random import *
from statistics import mean

#Constant for the number of elements we would like
NUM_OF_ELEMENTS = 20

#Create an empty list to store the elements
numbers = []

#Extra to store the aboce average numbers
above_average = []

#Create a for loop to prompt the user to enter a value with
#each iteration
for i in range(NUM_OF_ELEMENTS):
    #value = float(input("ENter a new number: "))
    #Randomly generate a floating point number
    value = randint(0,99) + round(random(),2)

    #Append value to the number list
    numbers.append(value)

#Compute the average
average = mean(numbers)

#Create a variable to count the above average numbers
count = 0

#for loop to iterate the same amount of times
#as we have indices
for i in range(NUM_OF_ELEMENTS):
    #check the current element against the average
    if numbers[i] > average:
        #append the value to our above average list
        above_average.append(numbers[i])

        #increment count by 1
        count += 1
#Sorting list in ascending/descending order
numbers.sort(reverse = True)
above_average.sort()

#Display the results
print(f"The numbers generated are:\n{str(numbers)[1:-1]}")
print(f"\nAverage is {average}")
print(f"\nNumber of elements above the average is {count}")
print(f"\nAbove average values are: \n{str(above_average)[1:-1]}")

    
