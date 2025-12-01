#Description: Calling a function to find the largest value

#Create a funtion to return the max between two integers
def max(num1,num2):

    #Check to see if first value is greater than second
    if num1 > num2:
        results = num1
    else:
        results = num2

    #Return the results back to the caller
    return results

#Create the main function
def main():

    #Initialize i, j, k
    i = 5
    j = 2
    k = max(i,j)  #Invoking the max function

    #Display the results
    print(f"The maximum between {i} and {j} is {k}")

#Invoke the main function
#This is where we start and end the program
main()
