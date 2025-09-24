#Testing out and, or, not opperators

#Prompt user to input integer value
number = int(input("Enter an integer: "))

#Check if number is divisible by 2 and 3
if number % 2 == 0 and number % 3 == 0:
    print(f"{number}, is divisible by 2 and 3")
    
#Check if the number is divisible by 2 or 3
if number % 2 == 0 or number % 3 == 0:
    print(f"{number}, is divisible by 2 or 3")

#Check if the number is divisible by 2 or 3 but not both
if (number % 2 == 0 or number % 3 == 0) and \
   not(number % 2 == 0 and number % 3 == 0):
    print(f"{number}, is divisible by 2 or 3, but not both")
    
