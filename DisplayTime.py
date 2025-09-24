#Obtains minutes and remaining seconds from an
#amount of time given by the user

#promt the user to input total seconds
seconds = int(input("Enter an integer for seconds: "))

#Get minutes and remaining seconds
minutes = seconds // 60
remaining_seconds = seconds % 60

#Display Results
print(seconds, "seconds is", minutes, "minutes and",
      remaining_seconds, "seconds")

print(f"{seconds} seconds is {minutes} minutes and \
{remaining_seconds} seconds")
