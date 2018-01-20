#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get and validate inputs from the user
    while True:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if(monthly_investment <= 0):
            print("Entry must be greater than 0. Please try again.")
        else:
            break

    while True:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if(0 >= yearly_interest_rate or yearly_interest_rate > 15):
            print("Entry must be greater than 0 and less than or equal to 15.")
        else:
            break

    while True:
        years = int(input("Enter number of years:\t\t"))
        if(0 >= years or years > 15):
            print("Entry must be greater than 0 and less than or equal to 50.")
        else:
            break
            

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        
        # display the result at and of year
        if((i + 1) % 12 == 0):
            year = int((i + 1) / 12)
            print("Year =  ", year, "\tFuture Value =  ", round(future_value, 2))
            
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
