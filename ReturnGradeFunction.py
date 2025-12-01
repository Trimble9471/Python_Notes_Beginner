#Description: Example of a return type function

#Create a function to return the grade back to the caller
def getGrade(score):

    #None special value to give control back to caller
    if score < 0 or score > 100:
        print("Invalid Score!")
        return None

    #Check the score for its letter grade
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

#Create main function
def main():

    #Prompt the user to input a test score
    score = float(input("Enter a score: "))

    #Display the results
    print(f"The letter grade is {getGrade(score)}")

#Invoke the main function
main()
