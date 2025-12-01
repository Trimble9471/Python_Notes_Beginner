#Description: Examples of default, positional, and keyword arguments

#Create a function to displayn the area
def print_area(width = 1,height = 2):

    area = width * height
    print(f"Width: {width} | Height: {height} | Area: {area}")

print_area()  #Default arguments width = 1 and height = 2
print_area(4,3)   #Positional arguments width = 4 height = 3
print_area(height = 5, width = 7)    #Keyword argument
print_area(12)
