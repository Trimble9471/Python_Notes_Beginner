#Testing our GCD Module and its 1 function

#import the module
from GCDFunction import gcd

#Prompt the user to input two integers
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))

#Display the results / incoke the gcd function
print(f"The greatest common divisor for {n1} and {n2} is {gcd(n1, n2)}")
