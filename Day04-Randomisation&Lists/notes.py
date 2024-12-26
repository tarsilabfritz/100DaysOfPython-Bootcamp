# Randomisation
import random  # 1° import the random module
random_integer = random.randint(1, 10)  # random.randint(a, b) = return a random number that is greater than or equal to a and less than or equal to b
print(random_integer)
random_float_0_to_1 = random.random()  # random.random() = return a random floating point number between 0.0 and 1.0
print(random_float_0_to_1)
random_float = random.uniform(1, 10)  # random.random() = return a random floating point number that is greater than or equal to a and less than or equal to b
print(random_float)

# The key difference between random.random() and random.uniform(a, b) lies in their range:
# random.random() = Generates a random floating-point number in the range [0.0, 1.0), where the value is inclusive of 0 and exclusive of 1
# random.uniform(a, b) = Generates a random floating-point number in the range [a, b], where both a and b are inclusive

# What is a module?
# A module in Python is a file containing Python code that can define functions, classes, variables, and runnable code. Modules are used to organize and reuse code across multiple programs.
# There are predefined modules provided by the language and there are custom modules that you can create by creating a code in a .py file and importing it into another script

import myModule
print(myModule.specific_number)

# Lists
# A list is a data structure where we can store grouped pieces of data
# In Python, lists always start with an open square bracket ([), the items separated by a comma, and a closing square bracket (])
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[0])  # Output: "Cherry"
print(fruits[1])  # Output: "Apple"
print(fruits[2])  # Output: "Pear"
print(fruits[-1])  # Output: "Pear"

fruits.append("Grape")  # list.append = add an item to the end of the list
print(fruits)

fruits.extend(["Papaya", "Apricot", "Kiwi"])
print(fruits)