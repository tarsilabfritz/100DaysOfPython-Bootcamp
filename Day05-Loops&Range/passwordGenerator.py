import random

# Variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Introduction
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

# Generate random characters for the password
password = []

for _ in range(nr_letters):
    password.append(random.choice(letters))
    
for _ in range(nr_symbols):
    password.append(random.choice(symbols))
    
for _ in range(nr_numbers):
    password.append(random.choice(numbers))

# Easy password (no shuffle)
# easy_password = ""
# for element in password:
    #easy_password += element 
easy_password = "".join(password)
print(f"Easy password: {easy_password}")

# Hard password (shuffle)
random.shuffle(password)
hard_password = "".join(password)  
print(f"Hard password: {hard_password}")

# NOTES:
    # The join() method:
        # - join() is a string method that takes a list of strings and concatenates them into a single string.
        # - The string used to call join() acts as a separator between the elements.
        # - In this case, "".join(password) uses an empty string as the separator, 
        #   meaning the elements are joined directly with no spaces or characters in between.
        # Example: If password = ['a', 'B', '1'], "".join(password) returns "aB1".
    # ---------------------------------------------------
    # The shuffle() method:
        # - shuffle() is a function from the random module that randomly rearranges the elements of a list.
        # - It modifies the list in-place, meaning the original list is updated with the shuffled order.
        # - shuffle() does not return a new list or any value; it just alters the existing list.
        # Example: If password = ['a', 'B', '1'], random.shuffle(password) could change it to ['B', '1', 'a'].