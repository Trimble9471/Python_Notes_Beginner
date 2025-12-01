'''
A recursive function is one that invokes itself (Direct Recursion)
'''

#Create a main function
def main():
    #Prompt the user to input a positive integer
    n = int(input("Enter a non-negative integer: "))

    #Display the results / invoke the factorial function
    print(f"Factorial of {n} is {factorial(n)}")

#Return the factorial for a specified number
def factorial(n):
    #Base case / stopping condition
    if n == 0:
        return 1
    else:
        #Recursive call, since we are invoking ourselves
        #We are decrementing n each call till we hit the base case
        return n * factorial(n - 1)

#Invoke the main function
main()
        
            
