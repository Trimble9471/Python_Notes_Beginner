#Determine whether a year is a leap year

#Prompt user to input a year
year = int(input("Enter a year:"))

#Check if the year is a leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or\
             (year % 400 == 0)

#Display the results
print(f"{year}, is a leap year? {isLeapYear}")
