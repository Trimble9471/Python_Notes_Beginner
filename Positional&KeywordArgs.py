'''
Two kinds of arguments: positional and keyword args

Positional: Will be passed in the same order as their
respective formal parameters.

Keyword: can appear in any order as you are assigning the value to
the formal parameter.

Note/Warning: You can mix these types: Positional will come before any keyword
arguments.
'''

#Function to display a message n times
def print_message(message,n):

    #Create a for loop to iterate n times
    for i in range(n):

        #Display the message
        print(message)

#Create main function
def main():

    #Invoke the print_message function and pass positional argument
    print_message("Welcome to Python", 5)
    print_message("Computer Science", 3)

    #Keyword arugment
    print_message(n = 5, message = "Hello, World")

    #Mixed both types
    #print_message("Hello World", n = 5)

#invoke the main function
main()
