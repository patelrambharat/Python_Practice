# variables is like jar that contains some value. we can store any value 
# in variable and we can use that value later in our program.  
my_variable = "bharat"
print(my_variable)  # prints the value of my_variable

# hey can I store Integer value, string value
x = 10
print(my_variable,x)  # prints the value of my_variable and x

y  = 5
print(x + y)  # prints the sum of x and y

# what if I want to add string
last_name = "patel"
print(my_variable + " " + last_name)  # prints the concatenation of my_variable and last_name

# can we add 10 with "bharat"?
#  print(10+my_variable)  # this will give error because we cannot add integer with string

# if we want to add integer with string then we need to convert integer into string using str() function
print(str(x) + my_variable)  # prints the concatenation of x and my_variable after converting x into string

# let's discuss multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)  # prints the values of x, y, and z

# if all the variable having the same value
x = y= z = 10
print(x, y, z)

'''this is the comment that I can use to write multiple lines of comment in python.
I can write anything here and it will not be executed by python interpreter.'''

total_sum = 10 + 20 + 30 + 40 + 50
print(total_sum)  # prints the total sum of the numbers

# if I wanted to press enter in between 10 , 20, 30 , 40 and 50 use /
total_sum = 10 + 20 + 30 + \
    40+50
print(total_sum)  # prints the total sum of the numbers

# what is indentation -> promotes the readability of the code. It is used to define the block of code. In python indentation is mandatory. If we don't use indentation then it will give error.

x=1
if(x == 1):
    print("wow")

print("wow")

# type casting: let's say I have a string value and I want to convert it into integer then we can use int() function to convert string into integer. Similarly we can use str() function to convert integer into string and float() function to convert integer into float.

a = 10
b = "10"
print(str(a) + b)  # prints the concatenation of a and b after converting a into string
print(type(a))  # prints the type of a

b_new = int(b)  # converts b into integer
print(a + b_new)  # prints the sum of a and b_new
print(type(b_new))  # prints the type of b_new

a_new = str(a)
print(type(a_new))  # prints the type of a_new
# this is called explicit type casting because we are explicitly converting the type of variable.

# implicit type casting: let's say I have a string value and I want to convert it into integer then we can use int() function to convert string into integer. Similarly we can use str() function to convert integer into string and float() function to convert integer into float.

a = 10
b = 10.5
c = a + b  # here a is integer and b is float so python will implicitly convert a into float and then add it with b
print(c)  # prints the sum of a and b
print(type(c))  # prints the type of c