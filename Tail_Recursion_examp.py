'''
Tail recursion example
'''

#Return the factorial for a specified number
def factorial(n):

    #Call/Invoke the auxillary function
    return factorialHelper(n,1)

#Auxillary tail-recursive function for factorial
#Stores the results for a factorial of n
def factorialHelper(n,result):

    #Base case / Stopping case
    if n == 0:
        return result
    else:
        #Recursive call
        return factorialHelper(n - 1,n * result)

#Create the main function
def main():
    #Prompt the user to input a positive integer
    n = int(input("Enter a non-negative integer: "))

    #Display the results / invoke the factorial function
    print(f"Factorial of {n} is {factorial(n)}")

#Invoke the main
main()
