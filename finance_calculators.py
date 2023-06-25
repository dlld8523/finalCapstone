# Program that allow the user to access two different financial calculators: 
# an investment caldulator and a home loan repayment calculator.
# The user choose which calculation they want to do.
# Set the user's input to lower case so that the programme is unaffected by the user's capitalization choice.

import math

print("investment-to calculate the amount of interest you'll earn on your investment")
print("bond      -to calculate the amount you'll have to pay on a home loan")
option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# If the user selects "investment", user will be asked to input amount of deposit, the interest rate and the number of years for investing 
# Then user asked to choose "compound" or "simple" interest
# Use the appropriate formula to calculate the total amount for investment 
# Output the amount that the user will get back after the given years

# If the user selects "bond", user will be asked to input present value of house, interest rate and number of months to repay
# Calculate with the formula and output the amount that user repay each month 

# If the user doesn't type in a valid input, display an error message

if option == "investment":
    deposit = float(input("Enter the amount of money that you are depositing: "))
    rate = float(input("Enter only the number of the interest rate e.g 7: ")) / 100
    years = float(input("Enter the number of years you plan to investing: "))
    interest = input("Do you choose 'compound' or 'simple' interest? ").lower()

    if interest == "simple":
        total = deposit * (1 + rate * years)
        print(f"Your total investment will be: {total} after {years} year")
    elif interest == "compound":
        total = deposit * math.pow((1 + rate), years)
        print(f"Your total investment will be: {total} after {years} year")
    else:
        print("Invalid input, please enter either 'simple' or 'compound'.")

elif option == "bond":
    value = float(input("Enter the present value of the house: "))
    rate = (float(input("Enter only the number of the interest rate e.g 7: ")) / 100) / 12
    months = float(input("Enter the number of months you plan to take to pay back the bond: "))

    repayment = (rate * value) / (1 - math.pow((1 + rate), -months))
    print(f"Your monthly bond repayment will be: {repayment} for {months} months")
else:
    print("Invalid input, please enter either 'investment' or 'bond'.")