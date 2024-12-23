# Subscripting is the method of 
print("Hello"[-1])

# Basic Data Types
# Strings (string concatenation)
print("123" + "345") 

# Integer = whole numbers
print(123 + 345)  

# Large integers (the underscore is just for reading)
print(123_456_789)  

# Float = floating point number
print(3.14159)  

# Boolean
print(True)
print(False)

# The type function allow us to check the data type of any piece of data
print(type("Dev"))  # <class 'str'>
print(type(2031))  # <class 'int'>
print(type(2.09))  # <class 'float'>
print(type(True))  # <class 'bool'>

# Type Casting is when you manually change the type of a data
print("123" + "456")  # String data type
print(int("123") + int("456"))  # Converts the strings "123" and "456" to integers and adds them, resulting in 579
# We can convert the data type using built-in functions, such as:
# int()
# float()
# str()
# bool()

# We used the str() built-in function because we can only concatenate str (not "int") to str
print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# Mathematical Operators
print(256 + 12)  # Addition
print(7 - 3)  # Subtraction
print(3 * 9)  # Multiplication
print(24 / 4)  # Division - Always results in a floating point number (Implicit Type Casting)
print(24 // 4)  # Floor Division - This division returns the integer part of the result
print(2 ** 3)  # Exponent - When you want to raise a number to a power
print(10 % 5)  # Modulo - Returns the remainder of a division

# PEMDAS = Parentheses, Exponents, Multiplication/Divison, Addition/Subtraction
print(3 * (3 + 3) / 3 - 3)

# The round function is used to round a floating point number to the nearest integer
floatNumber = 3.5999
print(round(floatNumber))  # Output: 4
print(round(floatNumber, 2))  # Output: 3.60 - because the second argument specifies the number of decimal places to round

# Number Manipulation
score = 0
score += 1  # It's the same as writing 'score = score + 1'
print(score)
score -= 2  # It's the same as writing 'score = score - 2'
print(score)
score *= 3  # It's the same as writing 'socre = score * 3'
print(score)
score /= -3  # It's the same as writin 'score = score / -3'
print(score)

# f-Strings allow us to embed variables directly into strings, making it easier to format and display dynamic content
# The variables are placed inside curly braces {} within the string, and the string is prefixed with 'f'
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. You are winnig is {is_winning}!")