# ==========================================
# FUNCTIONS IN PYTHON
# ==========================================

# A function is a reusable block of code 
# that performs a specific task.

# A function can:
# 1. Accept input values (parameters)
# 2. Perform some operation
# 3. Return a result (optional)

# Types of functions in Python:
# - Built-in functions  -> print(), len(), input(), etc.
# - User-defined functions -> Created by programmer using def keyword
# - Anonymous functions -> Created using lambda
# - Recursive functions -> Functions that call themselves


# ==========================================
# EXAMPLE 1: Without using function
# ==========================================

# Initialize variable x
x = 10

# Check whether x is greater than 10
if(x > 10):
    # Executes when condition is True
    print("greater than 10")
else:
    # Executes when condition is False
    print("IDK")


# ==========================================
# EXAMPLE 2: Code duplication problem
# ==========================================

# Same logic repeated again with another value
# This creates duplicate code

x = 12

if(x > 10):
    print("greater than 10")
else:
    print("IDK")

# If we need this logic many times,
# copying and pasting code is not a good practice.


# ==========================================
# SOLUTION: Use Function
# ==========================================

# Function definition
# p_x is the parameter received by function

def my_funct(p_x):

    # Check if passed value is greater than 10
    if(p_x > 10):

        # Executes when condition is True
        print("x is greater than 10")

    else:

        # Executes when condition is False
        print("IDK")


# Function calls (reusing same code)

my_funct(11)     # Passing 11
x = 11

my_funct(12)     # Passing 12
x = 12

my_funct(13)     # Passing 13


# ==========================================
# EXAMPLE 3: Function returning a value
# ==========================================

# This function checks condition
# and returns the passed value

def my_funct1(p_x):

    # Condition checking
    if(p_x > 10):
        print("x is greater than 10")
    else:
        print("IDK")

    # Return value back to caller
    return p_x


# Store returned value in variable
returned_val = my_funct1(20)

# Print returned value
print(returned_val)


# ==========================================
# DEFAULT ARGUMENT FUNCTION
# ==========================================

# Here b has default value = 30
# If user does not pass b, Python uses default value

def my_func2(a, b=30):
    return a + b


# Passing both arguments
# Default value 30 gets replaced by 3

sum = my_func2(2, 3)

print(sum)


# Scenario:
# b = 30 is already set as default

# But when we explicitly pass 60,
# Python overrides default value 30

sum = my_func2(20, 60)

print(sum)


# ==========================================
# *ARGS FUNCTION
# ==========================================

# * allows passing multiple values

# Python collects all values
# and stores them in tuple format

def my_func3(*a):

    # Returns all received values as tuple
    return a


# Passing multiple arguments

result = my_func3(10, 20, 30, 40)

print(result)


# Output:
# (10, 20, 30, 40)


# Explanation:
# *a means variable-length arguments

# Example:
# my_func3(1,2)
# my_func3(1,2,3,4,5,6)

# Python stores all values in tuple

# a = (10,20,30,40)

# ==========================================
# **KWARGS IN PYTHON
# ==========================================

# ** allows us to pass multiple keyword arguments
# (arguments with parameter names)

# Python stores these values in the form of a dictionary

# Function definition

def my_fun4(**px):

    # Print complete dictionary
    print(px, type(px))

    # Print only keys of dictionary
    print(px.keys())


# Function call

my_fun4(x=20, y=30, z=50)


# Output:
# {'x': 20, 'y': 30, 'z': 50} <class 'dict'>
# dict_keys(['x', 'y', 'z'])

# ==========================================
# LAMBDA FUNCTION IN PYTHON
# ==========================================

# Lambda function is also called an Anonymous Function

# Anonymous means:
# Function without a name

# It is generally used when we need a small function
# for a short period of time.

# Syntax:
# lambda arguments : expression


# ==========================================
# NORMAL FUNCTION
# ==========================================

# Function to add two numbers

def add(a, b):
    return a + b

result = add(10, 20)

print(result)


# ==========================================
# SAME USING LAMBDA FUNCTION
# ==========================================

# Lambda function for addition

add1 = lambda a, b: a + b

result = add1(10, 20)

print(result)

sub = lambda a, b : a-b
res  = sub(20, 10)
print(res)

# ==========================================
# EXAMPLE 2: Square of a number
# ==========================================

# Normal function

def square(x):
    return x * x

print(square(5))


# Using lambda

square1 = lambda x: x * x

print(square1(5))


# ==========================================
# EXAMPLE 3: Check even or odd
# ==========================================

# Lambda function with condition

check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))


# ==========================================
# EXAMPLE 4: Using lambda with sorted()
# ==========================================

# Sorting list based on second value

students = [
    ("Ram", 80),
    ("Shyam", 60),
    ("Mohan", 95)
]

# Sort using marks (index 1)

sorted_list = sorted(students, key=lambda x: x[1])

print(sorted_list)


# Output:
# [('Shyam', 60), ('Ram', 80), ('Mohan', 95)]


# ==========================================
# EXAMPLE 5: Using lambda with map()
# ==========================================

numbers = [1, 2, 3, 4, 5]

# Multiply each element by 2

result = list(map(lambda x: x * 2, numbers))

print(result)

# Output:
# [2, 4, 6, 8, 10]

#without lambda

print("without lambda ")
mylist = [1,2, 3, 4, 5]
def squarE(x):
    ret_list = [i * i for i in x]
    print(ret_list)
squarE(mylist)

mylist1 = [1,2, 3, 4, 5]

#Now using map
def square(y):
    return y*y
squareAns = list(map(square, mylist1))
print(squareAns)

#using lambda function
mylist2 = [1,2, 3, 4, 5]
print("with lambda ")
result = list(map(lambda x: x*x, mylist2))
print(result)



# ==========================================
# EXAMPLE 6: Using lambda with filter()
# ==========================================

numbers = [1, 2, 3, 4, 5, 6]

# Filter even numbers only

#similar to map 
result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

# Output:
# [2, 4, 6]

# reduce() reduces list to a single value

from functools import reduce

numbers = [1, 2, 3, 4]

# Add all numbers

result = reduce(lambda x, y: x + y, numbers)

print(result)

# Output: 10


