#Description: Default example plus list argument example
'''
#Create a function to append a new value to a list
def add(x, lst = []):

    if x not in lst:
        lst.append(x)

    #return the list back to the caller
    return lst
'''
#Default  none example
def add(x, lst = None):
    if lst == None:
        lst = []
    if x not in lst:
        lst.append(x)
    return lst

#Create main
def main():

    #Invoke the add function
    list1 = add(1)
    print(list1)

    list2 = add(2)
    print(list2)

    list3 = add(3, [11,12,13,14])
    print(list3)

    list4 = add(4)
    print(list4)

    
#invoke the main
main()
