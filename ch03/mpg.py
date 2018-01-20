#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

while True:
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))
    print()

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon, total cost and cost per mile
        mpg = round((miles_driven / gallons_used), 2)
        total_cost = round(gallons_used * cost_per_gallon, 1)
        cost_per_mile = round(total_cost / miles_driven, 1)

        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_cost)
        print("Cost_Per Mile:             ", cost_per_mile)
        print()

    # ask user if he wishes to continue
    choice = input("Get entries for another trip (y/n)? ")
    if(choice.lower() == "n"):
        break;

print()
print("Bye")



