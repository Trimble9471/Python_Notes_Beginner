#Main Function
def main():

    #Prompt the user to enter year and month
    year = int(input("Enter the full year (e.g., 2025): "))
    month = int(input("Enter the month as a number between 1 - 12: "))

    #Print calender for the month and year
    printMonth(year,month)

#Stub for printMonth
def printMonth(year,month):
    print(f"The year is {year} and the month is {month}")

#Stub for printMonthTitle
def printMonthTitle(year,month):
    pass

#Stub for the body
def printMonthBody(year,month):
    pass

#Stub for the name of the month
def getMonthName(month):
    pass

#Stub for the start day
def getStartDay(year,month):
    pass

#Stub for the total number of days
def getTotalNumberOfDays(year,month):
    pass

#Stub the number of days in the month
def getNumberOfDaysInMonth(year,month):
    pass

#Stub to see if it is a leap year
def isLeapYear(year):
    pass

#invoke the main function
main()

