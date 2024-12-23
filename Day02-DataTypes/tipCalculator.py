# Introduction
print("Welcome to the tip calculator!")

# Declaring variables
totalBill = float(input("What was the total bill? $"))
tipValue = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
peopleNumber = int(input("How many people to split the bill? "))

# Bill calculation
totalTip = (totalBill / 100) * tipValue
billPerPerson = (totalTip + totalBill) / peopleNumber

# Result
print(f"Each person should pay: ${round(billPerPerson, 2)}")