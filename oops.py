# ==========================================
# OOPS -> Object Oriented Programming
# ==========================================

# OOPS focuses on creating objects

# Class = Blueprint / Template
# Object = Real instance of class


# creating class
class Employee():

    # variables inside class = attributes

    emp_name = "bharat"
    emp_dept = "IT"

    # function inside class = method
    def info(self):

        # self is used to access class attributes
        print(f"Employee {self.emp_name} works for {self.emp_dept}")
        #whenever we will use attribute we will use self
        
            # function inside class = method
            #if we will pass the argument no need to provide self
    def infowithArg(self, emp_name, emp_dept):

        # self is used to access class attributes
        print(f"Employee {emp_name} works for {emp_dept}")
        #whenever we will use attribute we will use self
        #whenever we will using self we will use inner thing

# creating object
emp1 = Employee()

# accessing attribute
print(emp1.emp_name)

# calling method
emp1.info()

emp1.infowithArg("Rahul", "Mechanical")

# ==========================================
# CONSTRUCTOR IN PYTHON
# ==========================================

# Constructor = special method

# It automatically runs when object is created

# Used to initialize object values

# Constructor syntax -> __init__()


# ==========================================
# DEFAULT CONSTRUCTOR
# ==========================================

class Employee():

    # constructor
    def __init__(self):

        # runs automatically when object is created
        print("Constructor called")


# creating object
emp1 = Employee()


# Output:
# Constructor called


# ==========================================
# PARAMETERIZED CONSTRUCTOR
# ==========================================

class Employee():

    # constructor with arguments
    def __init__(self, name, dept):

        # initialize object variables
        self.name = name
        self.dept = dept


    # method
    def info(self):

        # access object variables
        print(f"Employee {self.name} works in {self.dept}")


# creating object
emp1 = Employee("Bharat", "IT")

# calling method
emp1.info()


# Output:
# Employee Bharat works in IT


# ==========================================
# MULTIPLE OBJECTS
# ==========================================

emp2 = Employee("Rahul", "Mechanical")

emp2.info()


# Output:
# Employee Rahul works in Mechanical

# ==========================================
# ATTRIBUTE IN PYTHON
# ==========================================

# Attribute = Variable inside a class

# Used to store data related to object

# Types:
# 1. Class Attribute
# 2. Instance Attribute


# ==========================================
# CLASS ATTRIBUTE
# ==========================================

class Employee():

    # class attributes
    company = "Accenture"
    dept = "IT"


# creating object
emp1 = Employee()

# accessing class attribute
print(emp1.company)
print(emp1.dept)


# Output:
# Accenture
# IT


# ==========================================
# INSTANCE ATTRIBUTE
# ==========================================

class Employee():

    # constructor
    def __init__(self, name, dept):

        # instance attributes
        self.name = name
        self.dept = dept


# creating objects
emp1 = Employee("Bharat", "IT")
emp2 = Employee("Rahul", "Mechanical")


# each object has different values
print(emp1.name)
print(emp2.name)


# Output:
# Bharat
# Rahul


# ==========================================
# MODIFY ATTRIBUTE
# ==========================================

class Employee():

    company = "Accenture"
    # static method
    # static method -> no self, no cls
    @staticmethod
    def add(a,b):
        return a+b

    # class method -> uses cls
    
      # class variable
    bonus = 10

    @classmethod
    def add1(cls, a, b):

        # using class variable in addition
        return a + b 
emp1 = Employee()

# changing attribute value
emp1.company = "Infosys"

# static method
sum = emp1.add(3,2)
print(sum)

# class method -> to interact directly to the class attribute
sum2 = emp1.add1(3,2)
print(sum2)
print(emp1.company)

# Output:
# Infosys

