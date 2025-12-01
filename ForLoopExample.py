#Testing out the for loop with sequences and the range function

#Iterating through a sequence
#A string is a sequence of characters. So are lists and tuples
#Known as sequence-type objects

#The variable i takes on each suvvessive value in the sequence
j = 0
for i in "Apple":
    print(f"Iteration: {j} | Element: {i}")

    #increment j by 1
    j += 1
print("\n")

#the function range(a,b - 1) returns a sequence of integers
#NOTE / WARNING: Range function can only take in integers

for i in range(4,8):
    print(i, end = ' | ')
print("\n")

#The range function has two more versions
#range(b-1)
#Defaults: will start at 0 and increment by 1
for i in range(5):
    print(i, end= ' | ')
print("\n")

'''
for i in range(100):
    print("Programming is fun!")
print("\n")
'''
#range(staringValue, endingValue - 1, step)
#range(a,b,k)
#The first # in sequence is (startingValue)
#each successive # in sequence will increase by (step)

i = 0
for value in range(3,10,2):
    print(f"Iteration: {i} | Value: {value}")
    i += 1
print("\n")
