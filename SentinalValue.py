#Read and calculate the sum of an unspecified
#number of integers

#Prompt the user to input an integer
data = int(input("Enter an integer (the input 0 exits the loop): "))

#Keep track of the running sum
sum = 0

#While loop to iterate until we input 0
while data != 0:

    #add integer to sum
    sum += data

    #reprompt user to input a integer
    data = int(input("Enter an integer (the input 0 exits the loop: "))

#Display the result
print(f"The sum is {sum}")
