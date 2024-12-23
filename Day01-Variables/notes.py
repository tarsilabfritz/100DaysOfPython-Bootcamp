# The print function is used to display messages or output data to the console
print("Hello world!")
print("Hello world!\nHello world!")
print("Hello, " + "Tarsila.") # string concatenation

# The input function is used to take input from the user via the console
input("What is your name? ")
print("Hello, " + input("What is your name? ") + "!") # the program will make the question first before displaying the whole sentence

# Variables are used to store data for future references and management
old = input("How old are you? ")
print("You are " + old + " years old.")

# The len function is used to calculate the length of a string (number of characters)
print(len(input("What is your last name? ")))
username = input("What is your username? ")
length = len(username)
print(length)
