'''
This approach compares the key element key sequentially with
each element in the list.

Note: We will return the index of where we find the element or
return -1 meaning we did not find the key
'''
#The function for finding a key in a list
def linearSearch(lst,key):

    #Iterate through each index of the list
    for i in range(len(lst)):
        #Check if the element is equal to the key
        if key == lst[i]:
            return i #Return index

    #Return -1 meaning key not found
    return -1
#Create main
def main():

    lst = [4,5,1,2,9,-3]
    print(linearSearch(lst,2))

#Invoke the main
main()
