'''
Note: Your list must be sorted before you search

Binary Search first compares the key with the element in the middle of
the list.

Case 1: If the key is less than the lists middle element you need to continue
the search for the key only in the first half.

Case 2: If the key is equal to the middle element return index

Case 3: If the key is greater than the lists middle element you need to continue
to search for the key only in the second half.
'''
#use binary search to find the key in the list
def binarySearch(lst,key):

    #Find and store the low and high index of our list
    low = 0
    high = len(lst) - 1

    #Create a while loop to iterate until high index is less than the low
    while high >= low:

        #Find the middle index
        mid = (low + high) // 2

        #Case 1
        if key < lst[mid]:
            high = mid - 1

        #Case 2
        elif key == lst[mid]:
            return mid  #Index of the middle element

        #Case 3
        else:
            low = mid + 1

    #Key not found
    return -1

#Create a main function
def main():

    lst = [-3, 1, 2, 3, 4, 9, 23]
    print(binarySearch(lst,2))

#Invoke the main
main()



        

        
