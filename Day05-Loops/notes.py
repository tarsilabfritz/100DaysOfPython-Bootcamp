# For Loop (associated with a list)
fruits = ["Apples", "Peach", "Pear"] # List of fruits
for fruit in fruits:
    print(fruit) # Prints each item in the list
    print(fruit + " pie") # Concatenates the item with the string " pie" and prints it
    
# General structure of a for loop:
# for item in list_of_items:
#     Do something with item

# ---------------------------------------------------

# Sum of a list of numbers
student_scores = [150, 142, 183, 120, 171, 184, 149, 24, 59] # LIst of student score

# Using the built-in sum() function to calculate the total
total_exam_score = sum(student_scores)
print(total_exam_score)

# Using a for loop to calculate the sum manually
sum_manual = 0
for score in student_scores: 
    sum_manual += score # Adds each score to the running total
print(sum_manual) # Prints the manually calculated total

# ---------------------------------------------------

# Finding the maximum value in a list
# Using the built-in max() function
max_exam_score = max(student_scores)
print(max_exam_score) # Prints the maximum score

# Using a for loop to find the maximum manually
max_manual = 0
for score in student_scores:
    if score > max_manual:  # Compares each score with the current maximum
        max_manual = score  # Updates the maximum if a larger score is found
print(max_manual)  # Prints the manually found maximum score

# ---------------------------------------------------

# For loops with the range() function
# The range() function generates a sequence of numbers:
# range(a, b): Generates numbers from a (inclusive) to b (exclusive)
# range(a, b, step): Generates numbers from a to b, incrementing by step

# Example: Generating numbers from 1 to 9
for number in range(1, 10):  # The range goes from 1 to 9 (10 is excluded)
    print(number)  # Prints each number in the range

# Example: Generating numbers with a step of 3
for number in range(1, 10, 3):  # Numbers start at 1 and increment by 3
    print(number)  # Prints each number (e.g., 1, 4, 7)

# ---------------------------------------------------

# Key Notes:
# 1. Built-in functions like sum() and max() simplify operations and are preferred when readability and efficiency are priorities.
# 2. Manual calculations (using loops) are useful for understanding the logic behind these operations.
# 3. The range() function is a powerful tool for generating sequences, especially when combined with loops.