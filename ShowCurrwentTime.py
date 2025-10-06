#Obtain current time and compute the current
#seconds, minutes, and hours.

#Import the time module
import time

#Obtain the current time by invoking time function
currentTime = time.time()
print(currentTime)

#Obtain the total seconds
#By using int() function we can drop the decimal
totalSeconds = int(currentTime)
print(totalSeconds)

#Compute the current seconds from our total sec value
currentSeconds = totalSeconds % 60

#Compute the total minutes
totalMinutes = totalSeconds // 60

#Compute the current minutes from total minutes
currentMinutes = totalMinutes % 60

#Compute the total hours
totalHours = totalMinutes // 60

#Compute the current hour
currentHours = totalHours % 24

#Display the results
print(f"Current time is {currentHours}:{currentMinutes}:\
{currentSeconds} GMT")


