#Description: Returning multiple values back from a function and
#assigning them to a multiple variables (Simultaneous assignment)

#Create a function to sort values in ascending order
def sort(num1,num2):

    #Check if num1 is less than num2
    if num1 < num2:
        return num1,num2
    else:
        return num2,num1

#Using S.A to store multiple values
n1,n2 = sort(4,2)   #Invoking the sort function

#Display the values
print(f"N1 = {n1} | N2 = {n2}")
