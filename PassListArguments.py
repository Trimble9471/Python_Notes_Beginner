#Create main function
def main():
    x = 1 #x represents an integer object (immutable object)
    y = [1,2,3] #y represents a list object (mutable object)

    #Invoke m with arguemnt x and y
    m(x,y)

    #Display the values of x and y
    print(f"x is {x}")
    print(f"y[0] is {y[0]}")

#Create a function to change the value of the integer and list
def m(number,numbers):
    number = 1001 #Assign a new value to number
    numbers[0] = 5555 #Assign a new value to index 0

#invoke the main function
main()

