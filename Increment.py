#Description: Example of passing arguments by its reference value

#Create main function
def main():

    #initialize x to 1
    x = 1

    #Display the value of x before invoking increment function
    print(f"Before the call/invoke, x is {x}")

    #Invoke the increment function
    increment(x)

    #Display the results after the function call
    print(f"After the call/invoke, x is {x}")

#Create the increment function to add 1 to the reference value
def increment(n):

    #Add 1 to n
    n += 1

    #Display the value of n
    print(f"\t\n inside the function n is {n}")

#Invoke the main function
main()
