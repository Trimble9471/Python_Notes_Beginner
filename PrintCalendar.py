#import system
import sys

#Main Function
def main():

    #Prompt the user to enter year and month
    year = int(input("Enter the full year (e.g., 2025): "))
    month = int(input("Enter the month as a number between 1 - 12: "))

    #Print calender for the month and year
    printMonth(year,month)

#Stub for printMonth
def printMonth(year,month):

    #Print the headings of the calendar
    printMonthTitle(year,month)

    #print the body of the calendar
    printMonthBody(year,month)

#Stub for printMonthTitle
def printMonthTitle(year,month):
    print(f"{' ':9s}" , getMonthName(month), ' ', year)
    print('-' * 29)
    print(" Sun Mon Tue Wed Thu Fri Sat")

#Stub for the body
def printMonthBody(year,month):
    #Get the start day of the week for the first date in month
    startDay = getStartDay(year,month)

    #Get number of days in the month
    numberOfDaysInMonth = getNumberOfDaysInMonth(year,month)

    #Pad space before the first day
    i = 0
    for i in range(startDay):
        print(f"{' ':4s}", end = '')

    for i in range(1, numberOfDaysInMonth + 1):
        print(f"{i:4d}", end + '')

        if (i + startDay) % 7 == 0:
            print() #Jump to the next line

#Stub for the name of the month
def getMonthName(month):

    match month:
        case 1: monthName = "January"
        case 2: monthName = "February"
        case 3: monthName = "March"
        case 4: monthName = "April"
        case 5: monthName = "May"
        case 6: monthName = "June"
        case 7: monthName = "July"
        case 8: monthName = "August"
        case 9: monthName = "September"
        case 10: monthName = "October"
        case 11: monthName = "November"
        case 12: monthName = "December"
        case _: sys.exi("Invalid Object")

    return monthName #return back to the caller


#Stub for the start day
def getStartDay(year,month):
    START_DAY_FOR_JAN_1_1800 = 3

    #Get the total number of days from 1/1/1800
    totalNumberOfDays = getTotalNumberOfDays(year,month)

    #Return the start day for month/1/year
    return (totalNumberOfDays + START_DAY_FOR_JAN_1_1800) % 7

#Stub for the total number of days
def getTotalNumberOfDays(year,month):
    total = 0

    #Get the toal days from 1800 to 1/1/year
    for i in range(1800,year):
        if isLeapYear(i):
            total += 366
        else:
            total += 365

    #Add days from jan to the month prior to the calendar month
    for i in range(1,month):
        total = total + getNumberOfDaysInMonth(year,i)

    #return the total back to caller
        return total
    

#Stub the number of days in the month
def getNumberOfDaysInMonth(year,month):

    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12: return 31
        case 4 | 6 | 9 | 11: return 30
        case 2: return 29 if isLeapYear(year) else 28
        case _: return 0 #If month is incorrect

#Stub to see if it is a leap year
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


#invoke the main function
main()


