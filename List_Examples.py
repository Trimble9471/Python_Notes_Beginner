'''
Creating lists
The elements in a list are separated by a comma.
Lists are enclosed by a pair of square brackets []
Lists can contain the elements of the same type or mixed types
Lists are mutable (contents can be changed)
Lists can grow and shrink on demand
'''

#Create an empty list
list1 = []
print(type(list1), list1)

#Create a list of 10 elements of 0
list1 = [0] * 10
print(type(list1), list1)

#Create a list of integers
list2 = [1,2,3,4,5]
print(list2)

#Create a list of strings
list3 = ["red","green","blue"]
print(list3)

#Strings and Lists are sequence types in Python
#A list is a sequence of any element
list4 = [3,True,3.6,"okay"]
print(type(list4), list4)

#List() function creats a list object
#Syntax: list(iterable) or list(<iter>)
#Note: In python, iterable means an object can be used in iteration

#Create an empty list
list5 = list()
print(type(list5), list5)

#list6 = list(1,2,3)

list6 = list([1,2,3])
print(list6)

list7 = list(range(3,7))
print(list7)

list8 = list("abcd")
print(list8)

#Functions for lists
import random

#Len() function returns the number of elements in the list
list1 = [2,3,4,1,22]
print(f"Len(list1) = {len(list1)}")
print("Len(list1) =", len(list1))

#Max() function returns the largest element
print("max(list1) =", max(list1))

#Min() function returns the smallest element
print("min(list1) =", min(list1))

#Random.shuffle() will shuffle the elements randomly in the list
random.shuffle(list1)
print(list1)

#Index operator []
#An element in a list can be accessed through the index operator
#Syntax: myList[index]
#Note: index range from 0 to len(myList) - 1
myList = [5.6, 4.5, 3.3, 13.2, 4.0, 34.33, 34.0, 45.45, 99.99]

#Index operator can be used just like a variable
myList[2] = myList[0] + myList[1]
print(myList)

#You can also iterate through a list
for i in range(len(myList)):
    myList[i] = i #Changing the eleemtns to its index value
print(myList)

#Python allows the use of negative numbers as indexes to
#reference positions relative to the end of the list
print(list1[-1])
print(myList[-3])

#List Slicing [starting index : end index - 1 : step value]
#Note: if the start index is left empty its default is 0
#Note: if the end index is left empty its default is len(list) - 1
list1 = [2,3,5,7,9,1]
print(list1[2:4])
print(list1[ : 5 : 2])
print(list1[3: ])

#You can assign values to a slice of a list
list1[1:3] = [91,92,93,94]
print(list1)

#The +, *, in, not in operators
list1 = [1,2]
list2 = [3,4]

#Create a list by concatenating list1 and list2 together
list3 = list1 + list2
print(list3)

list4 = list3 * 3 #Concatenating the same string 3 times
print(list4)

list3 + [7,8] == list3 #will append the new list to the end
print(list3)

print(2 in list1)
print(2 not in list1)

#You can traverse the list sequentially without using an index variable
for i in list3:
    print(i)
print()

#List comprehensions is a concise syntax that creates a list
#by processing another sequence of data
list1 = [x for x in range(5)]
print(list1)

list2 = [0.5 * x for x in list1]
print(list2)

list3 = [x for x in list3 if x < 1.5]
print(list3)

#Splitting a string into a list
list1 = list("a,b,c")
print(list1)

#The string classs contains the split method
#which will split itmes in a string into a list
#you can use a nonspace delimiter or a space delimiter to seperate elements
items = "car plane train".split()
print(items)

date = "11/10/2025".split('/')
print(date)
'''
#Inputting a list
#first way you can enter one data item per line and append it to the list
list1 = []
print("Enter 5 numbers, one number per line: ")
for i in range(5):
    list1.append(int(input()))
print(list1)

#or we can take in a string and use the split method and list comprehensions
s = input("Enter 5 numbers seperated by 1 space: ")
items = s.split() #Extracts items from the string
list1 = [int(x) for x in items] #Convert string data types to integers
print(list1)
'''
#Methods from the list class
#append method adds an element to the end of the list
list1 = [2,3,4,1,32,4]
list1.append(55)
print(list1)

#Count method returns the number of times that element appears in the list
print(list1.count(4))

#extend method appends all the elements in another list to the current list
list2 = [99,1]
list1.extend(list2)
print(list1)

#index method returns the index of the first occurance
print(list1.index(4))

#Insert method inserts a element at a specified index
list1.insert(0,25)
print(list1)

#remove method will remove the first occurence of the element
list1.remove(4)
print(list1)

#reverse method will reverse the order of your elements
list1.reverse()
print(list1)

#sort method will sort your list in ascending order
list1.sort()
print(list1)

#descending order
list1.sort(reverse = True)
print(list1)

#Python statistics module
#We can perform statistics tasks on lists, tuples, and sets
from statistics import *

list1 = [1,2,3,4]
print(mean(list1)) #returns the average

list2 = [1,8,7,3,2]
print(median(list2)) #returns our middle value (sorted)

list3 = [7,1,8,7,3,2]
print(mode(list3))





