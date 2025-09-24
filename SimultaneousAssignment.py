#Python simultaneous assignment statements allows
#multiple values to be assigned to the equal number of varialbes
#at the same time.

#assign values to three variable
num1, num2, num3 = 1, 2, 3

#Promt the user to input 3 values
#Note: NOT SECURE

#num1, num2, num3 = eval(input("Enter three values \
#seperated by a comma: "))

#Compute the average
average = (num1 + num2 + num3) / 3

#Display the results
print("The average is", average)

#Swapping a Value
x = 1
y = 2

x,y = y,x

print("The value of x is", x, "and the value of y is", y)
