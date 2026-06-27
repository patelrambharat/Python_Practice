# ==========================================
# GETTER AND SETTER IN PYTHON
# ==========================================

# Getter -> used to get/read value

# Setter -> used to set/update value

# Mostly used for Encapsulation
# (restrict direct access to variables)


# ==========================================
# BASIC EXAMPLE
# ==========================================

class Employee():

    # constructor
    def __init__(self):

        # private variable
        # __ makes variable private
        self.__salary = 50000


    # getter method
    def getSalary(self):

        # returns value
        return self.__salary


    # setter method
    def setSalary(self, salary):

        # updating value
        self.__salary = salary


# object creation
emp1 = Employee()


# getter -> read value
print(emp1.getSalary())

# Output -> 50000


# setter -> change value
emp1.setSalary(70000)


# getter again
print(emp1.getSalary())

# Output -> 70000


# ==========================================
# WHY PRIVATE VARIABLE ?
# ==========================================

# direct access is restricted

class Employee():

    def __init__(self):

        # private variable
        self.__age = 25


obj = Employee()

# this will give error
# print(obj.__age)


# ==========================================
# VALIDATION USING SETTER
# ==========================================

# setter can add conditions before updating value

class Student():

    def __init__(self):

        self.__marks = 0


    # setter
    def setMarks(self, marks):

        # validation
        if marks >= 0:

            self.__marks = marks

        else:
            print("Invalid marks")


    # getter
    def getMarks(self):

        return self.__marks


s1 = Student()

s1.setMarks(90)

print(s1.getMarks())

# Output -> 90


s1.setMarks(-5)

# Output -> Invalid marks