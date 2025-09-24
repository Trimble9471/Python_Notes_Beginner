#Create a program that displays the sales tax with 2 digits after decimal

#Prompt the user to input the purchase amount
purchaseAmount = float(input("Enter purchase amount: "))

#compute the sales tax
tax = purchaseAmount * 0.06

#display the results
print("Sales tax is", int(tax * 100) / 100)

#print("Sales tax is", round(tax,2))


'''
input is 197.55
tax = 1185

tax * 100 is 1185.3
int(tax * 100) = 1185
int(tax * 100) / 100 = 11.85
'''
