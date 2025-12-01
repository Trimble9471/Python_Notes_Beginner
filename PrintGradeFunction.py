#Description: Example of a non return type function

#Create a function to find the letter grade from a test score

def printGrade(score):

    #Multi way if to determine its letter
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')

#Create main function
def main():

    #Prompt the user to input a test score
    score = float(input("Enter a score: "))

    #Display the results invoke the printGrade function
    print("The letter grade is ", end = '')
    printGrade(score)

#Invoke the main function
main()
