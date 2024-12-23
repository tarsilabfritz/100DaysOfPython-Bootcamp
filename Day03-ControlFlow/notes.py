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

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    # Ticket price
    if age >= 18:
        print("Your ticket will be $12.")
    elif age >= 12:
        print("Your ticket will be $7.")
    else:
        print("Your ticket will be $5.")
else:
    print("Sorry you have to grow taller before you can ride.")