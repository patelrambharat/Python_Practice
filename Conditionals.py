# take input from user
x = int(input("Enter a number: "))  # takes input from user and converts it into integer
if(x == 10):
    print("x is equal to 10")   # prints "x is equal to 10" because the condition is true
elif(x > 10):
    if(x > 20):
        print("x is greater than 20")  # this will not be executed because the condition is false
    print("x is greater than 10")  # this will not be executed because the condition is false
else:
    print("x is not equal to 10")  # this will not be executed because the condition is false
# difference between if and elif is that if will be executed only if the condition is true and elif will be executed only if the previous condition is false and the current condition is true.

if(x % 2 == 0):
    print("x is even")  # prints "x is even" if x is divisible by 2
else:
    print("x is odd")  # prints "x is odd" if x is not divisible by 2