#Description: Keyword break will break out of the loop

#Track the total
total = 0
number = 0

#Create a while loop to iterate 20 times
while number < 20:
    #add 1 to number
    number += 1
    #add number to total
    total += number
    #if sum is greater than or equal to 100 break
    if total >= 100:
        break #exit loop
#Display
print(f"The number is {number}")
print(f"The total is {total}")
