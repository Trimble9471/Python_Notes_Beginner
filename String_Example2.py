#The string class methods for manipulating strings
#Table 4.5 Methods for testing its characters
s = "Welcome to Python"

#isalnum() returns True if all characters in the string
#are alphanumeric and there is atleast 1 character (a-z)(0-9)
print(s.isalnum())

#isdigit() returns true if the string contains only digits
print("1234".isdigit())

#islower() and isupper() returns true if letters are either way
print("abs".islower())
print("ABC".isupper())
'''
s = input("Enter your age: ")

if s.isdigit():
    print("Age: ", s)
else:
    print("Error")
'''

#Table 4.6 Methods for searching substrings
#endswith() and startswith()
print(s.endswith("thon"))
print(s.startswith("become"))

#find(s) returns the lowest index where s starts
#rfind(s) returns the highest index where s starts
#Note: Will get -1 if not found
print(s.find("Wel"))
print(s.rfind("Help"))

#count() returns the number of non-overlapping occurences
print(s.count("o"))

#Table 4.7 methods for converting letter casses in strings
print("WELCOME".lower())
print("welcome".upper())
print("welcome".capitalize())
print("welcome to python".title())
print("WeLcOmE".swapcase())
print("Hello".replace("Hello","Hi"))

#Table 4.8 methods for stripping whitespace characters
s1 = "\tWelcome to Python\t\n"
print(s1.lstrip()) #Removes the left whitespace characters
print(s1.rstrip()) #Removes the right whitespace characters
print(s1.strip()) #Removes both sides

#s = input("Enter your names: ").strip() 
