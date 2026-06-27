#Exception handling
# ==========================================
# EXCEPTION HANDLING IN PYTHON
# ==========================================

# Exception = Error that occurs during program execution

# Used to prevent program from crashing

# Keywords:
# try      -> risky code
# except   -> handles error
# else     -> runs if no error
# finally  -> runs always


x = "10"
try:
    if(x > 10):
        print("number is greater that 10")
    else:
        print("IDK")
except:
    print("error occured")
    
# ==========================================
# TRY - EXCEPT
# ==========================================

# code that may cause error

try:
    
    # division by zero error
    a = 10 / 0

# handles the error
except:
    print("Error occurred")


# ==========================================
# SPECIFIC EXCEPTION
# ==========================================

try:
    
    num = int("abc")      # invalid conversion

# handles ValueError only
except Exception as e:
    print(e)


# ==========================================
# ELSE BLOCK
# ==========================================

# runs only when no exception occurs

try:
    
    num = 10 / 0

except Exception as e:
    print("Error" , e)

else:
    print("No error")


# ==========================================
# FINALLY BLOCK
# ==========================================

# always executes

try:
    
    num = 10 / 0

except:
    print("Error")

finally:
    print("Always runs")


# ==========================================
# MULTIPLE EXCEPT
# ==========================================

try:
    
    x = int("abc")

except ValueError:
    print("Value Error")

except ZeroDivisionError:
    print("Division Error")


# ==========================================
# CUSTOM EXCEPTION
# ==========================================

# manually raise exception

age = -5

try: 
    if age < 0:
        raise Exception("Age cannot be negative")
except Exception as e:
    print(e)

#Now abstring

name = "bharat"
my_string = "Hello my name is bharat how are you"
print(my_string)

#now at the place on bharat I wanted to use name variable
my_string1 = f"Hello my name is {name} how are you"
print(my_string1)

try:
    
    num = int("abc")      # invalid conversion

# handles ValueError only
except Exception as e:
    print(f"hey you got this error {e}")  #we can use like this 


def my_func(p_x):

    print("Hello World")

    try:
        if(p_x % 2 == 0):
            return 1

    except Exception as e:
        return e

    #print("Hello World") # if we will not use finally then it will not print this because in the python if we got the return it will break
    #so now we will use finally
    finally:
        print("hello")

my_func(4)

#global variable
# ==========================================
# GLOBAL VARIABLE IN PYTHON
# ==========================================

# Global variable = variable declared outside function
# Can be accessed anywhere in program


# global variable
x = 10


# function accessing global variable
def my_func():

    # accessing global variable
    print(x)


my_func()

# Output -> 10


# ==========================================
# MODIFYING GLOBAL VARIABLE
# ==========================================

# global variable
count = 5


def update():

    # tells Python to use global variable
    global count

    # modifying global variable
    count = count + 1


update()

print(count)

# Output -> 6


# ==========================================
# LOCAL VARIABLE
# ==========================================

# variable inside function = local variable

def demo():

    # local variable
    y = 20

    print(y)


demo()

# print(y) -> Error (outside function)


# ==========================================
# GLOBAL vs LOCAL
# ==========================================

# global variable
a = 100


def test():

    # local variable
    a = 50

    # local value
    print(a)


test()

# global value
print(a)


# Output:
# 50
# 100

#enumerator
my_list = [100, 200, 300, 400, 500]
for i,x in enumerate(my_list):
    print(i,x)