#Predicting the future tuition until the tuition has doubled
#Note: Our tuition for a university is $10,000 this year'
#Note: Will increase 7% annually

tuition = 10000
year = 0

#Create a while loop and set its condition to exit when tuition has doubled
while tuition < 20000:
    tuition *= 1.07  #apply interest
    year += 1  #Increment to the next year
print(f"Tuition will be doubled in {year} years")
print(f"Tuition will be ${tuition:.2f} in {year} years")

########################################################################
#For loop

#Create a exit variable to be checked
target_tuition = 20000

#Reinitialize tuision and year to double
tuition = 10000
year_to_double = None

#Create for loop to iterate a large number
for year in range(1,101):
    #Apply 1 years growth
    tuition *= 1.07

    #Check whether we have reached or passed the target
    if tuition >= target_tuition:
        year_to_double = year
        break
if year_to_double is not None:
    print(f"Tuition will be doubled in {year_to_double} years")
    print(f"Tuition will be ${tuition:.2f} in {year_to_double}")
