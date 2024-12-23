# Control Flow 

# Condition if / else:
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

# Nested if/else statement = is a programming structure that places an if/else statement inside another if/else statement

# Comparison Operators:
# > (Greater than)
# < (Less than)
# >= (Greater than or equal to)
# <= (Less than or equal to)
# == (Equal to)
# != (Not equal to)

# Multiple if VS. if / elif / else
# Multiple if executes all true conditions independently, while if/elif/else checks conditions sequentially and stops at the first true condition

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    # Age and photo (multiple if)
    # Ticket price (if/elif/else statement)
    if age >= 45 and age <= 55:  # or "45 <= age <= 55"
        print(f"Everything is going to be ok. Have a free ride on us!")
    elif age >= 18:
        bill = 12
        print(f"Adult tickets are ${bill}.")
    elif age >= 12:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    else:
        bill = 5
        print(f"Child tickets are ${bill}.")
        
    wantsPhoto = input("Do you want to have a photo take? Type y for Yes and n for No. ")
    if wantsPhoto == "y":
        bill += 3
        
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
    
# Logical operators for multiple conditions
# and = True only when both conditions are true
# or = True when at least one condition is true
# not = Reverses the truth value of a condition