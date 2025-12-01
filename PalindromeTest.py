'''
Palindrome Checker: palindrome reads same forwards and backwards

Note: case-sensitive (so Racecar is not racecar)
Note: space/punctuation sensitve
'''

#Prompt the user to inter a string
s = input("Enter a string: ")

#low variable will track the index at the left side of the string
low = 0

#high variable will track the index at the right side of the string
high = len(s) - 1

#Assume the string is a palindrome until proven otherwise
isPalindrome = True

#Continue comparing while the left indext is strictly less than the right
while low < high:

    #If the characters at current ends dont match cant be palindrome
    if s[low] != s[high]:
        isPalindrome = False
        break  #Exit early

    #if they do match, increment the low index and decrement high
    low += 1
    high -= 1

#After the loop display results
if isPalindrome:
    print(f"{s} is a palindrome!")
else:
    print(f"{s} is not a palindrome!")
