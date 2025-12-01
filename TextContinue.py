#Description: Continue keyword will skip everything below it
#inside the loop body and go to the next iteration

#track total
total = 0
number = 0

#Create while loop to iterate 20 times
while number < 20:

    #add 1 into number
    number += 1

    #We do not want to add 10 or 11 into the total
    if number == 10 or number == 11:
        continue #So everyting below this point is skp

    #add our number to total
    total += number

#Display
    print(f"The total amound is {total}")
