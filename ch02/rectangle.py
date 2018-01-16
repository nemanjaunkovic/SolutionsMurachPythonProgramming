#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
length = int(input("Please enter the length: "))
width  = int(input("Please enter the width:  "))

# calculate area and perimeter
area = length * width
perimeter = (length + width) * 2
            
# format and display the result
print()
print("Area = ", area)
print("Perimeter = ", perimeter)
print()
print("Thanks for using this program!")


