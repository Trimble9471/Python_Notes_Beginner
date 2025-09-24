#Computing and interpreting BMI for people 16 years +
'''
Conversion values
Note: 1 pound is 0.45359237 kilograms
Note: 1 inch is 0.0254 meters
'''

#Name constants for conversion values
KILO_POUND = 0.45359237
METERS_INCH = 0.0254

#Prompt user to enter their weight in pounds
weight = float(input("Enter weight in pounds: "))

#Prompt user to enter their height in inches
height = float(input("Enter height in inches: "))

#Compute the BMI after we convert weight and height
weightInKilograms = weight * KILO_POUND
heightInMeters = height * METERS_INCH

bmi = weightInKilograms / (heightInMeters ** 2)

#Display the results using Multi-way
print(f"BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

    
      
