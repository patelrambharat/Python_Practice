# ==========================================
# INHERITANCE IN PYTHON
# ==========================================

# Inheritance = one class acquires properties
# and methods of another class

# Parent Class -> Base class
# Child Class -> Derived class

# Reusability is the main advantage


# ==========================================
# SINGLE INHERITANCE
# ==========================================

# parent class
class Employee():
    def work(self):
        print("Employee is working")
# child class inherits parent class
class Developer(Employee):
    def code(self):
        print("Developer is coding")
# object of child class
obj = Developer()

# inherited method
obj.work()

# child method
obj.code()

#parent method
class Dog():
    def speak(self):
        print("Dog is barking")
class Cat(Dog):
    def cry(self):
        print("Cat is crying")
obj1 = Cat()
obj1.cry()
obj1.speak()
# Cat is crying
# Dog is barking
# Output:
# Employee is working
# Developer is coding

class company():
    def company_info(self):
        print("company name is xyz")
class employee(company):
    def emp_info(self):
        print("employee name is bharat")
        
emp1 = employee()
emp1.emp_info()
emp1.company_info()


# ==========================================
# USING CONSTRUCTOR IN INHERITANCE
# ==========================================

# parent class
class Employee():
    def __init__(self, name):

        self.name = name
# child class
class Developer(Employee):

    def show(self):

        print(self.name)
# object creation
obj = Developer("Bharat")

obj.show()
# Output:
# Bharat
# using constructor
# Parent class
class Comp():

    # constructor of parent class
    def __init__(self, comp_name):  

        # storing company name
        self.comp_name = comp_name


    # parent method
    def companyinfo(self):

        # printing company name
        print(f"company name is {self.comp_name}")


# Child class inheriting parent class
class emp(Comp):

    # child constructor
    def __init__(self, emp_name, comp_name):

        # storing employee name
        self.emp_name = emp_name

        # storing company name directly
        # here we are NOT calling parent constructor
        # self.comp_name = comp_name
        # at the place of the above we can use this 
        Comp.__init__(self,comp_name)   #so like this we can call the company name if there is so many attribute we no need to write self. self. multiple time
        
        
        # # calling parent constructor
        # super().__init__(comp_name)   we can use the super keyword to access the function from parent class


    # child method
    def empinfo(self):

        # printing employee name
        print(f"employee name is {self.emp_name}")
    def cominfo_child(self):
        print("this is running from employee")
        Comp.companyinfo(self)       #like this we can call the comapny method in the child class

# creating object of child class
emp2 = emp("rahul", "Accenture")

# calling child method
emp2.empinfo()

# calling inherited parent method
emp2.companyinfo()
emp2.cominfo_child()
# ==========================================
# MULTILEVEL INHERITANCE
# ==========================================

# Grandparent
class A():

    def showA(self):
        print("Class A")


# Parent
class B(A):

    def showB(self):
        print("Class B")


# Child
class C(B):

    def showC(self):
        print("Class C")


obj = C()

obj.showA()
obj.showB()
obj.showC()


# Output:
# Class A
# Class B
# Class C

# example 2 :

# Grandparent Class: Base device layer
class BasicWatch:
    def __init__(self, brand):
        self.brand = brand

    def show_time(self):
        return f"[{self.brand}] Displaying standard local time."
    
# Parent Class: Adds modern connectivity (Inherits from BasicWatch)
class ConnectedWatch(BasicWatch):
    def __init__(self, brand, wifi_enabled=True):
        super().__init__(brand)  # Triggers BasicWatch initialization
        self.wifi_enabled = wifi_enabled

    def sync_notifications(self):
        return "Syncing enterprise emails and calendar alerts."   
    
# Child Class: Adds health sensors (Inherits from ConnectedWatch)
class EnterpriseSmartWatch(ConnectedWatch):
    def __init__(self, brand, wifi_enabled, target_steps=10000):
        super().__init__(brand, wifi_enabled)  # Triggers ConnectedWatch initialization
        self.target_steps = target_steps

    def track_heart_rate(self):
        return f"Tracking heart rate. Daily step goal: {self.target_steps}."
# --- Real-Time Execution ---
corporate_device = EnterpriseSmartWatch(brand="AppleWatch Corporate", wifi_enabled=True, target_steps=12000)

print(corporate_device.show_time())           # Inherited from Grandparent (BasicWatch)
print(corporate_device.sync_notifications())   # Inherited from Parent (ConnectedWatch)
print(corporate_device.track_heart_rate())     # Defined in Child (EnterpriseSmartWatch)
# ==========================================
# MULTIPLE INHERITANCE
# ==========================================

# one child inherits multiple parents



class A():

    def showA(self):
        print("Class A")


class B():

    def showB(self):
        print("Class B")


# child inherits A and B
class C(A, B):

    def showC(self):
        print("Class C")


obj = C()

obj.showA()
obj.showB()
obj.showC()



# example 2
# Parent Class 1: Handles timekeeping features
class Clock:
    def __init__(self, time_zone="UTC"):
        self.time_zone = time_zone

    def show_time(self):
        return f"Displaying current time in {self.time_zone} format."
# Parent Class 2: Handles wellness tracking features
class HealthTracker:
    def __init__(self, target_steps=10000):
        self.target_steps = target_steps

    def track_heart_rate(self):
        return "Measuring heart rate: 72 BPM."
# Child Class: Combines both capabilities using multiple inheritance
class SmartWatch(Clock, HealthTracker):
    def __init__(self, brand, time_zone, target_steps):
        # Initializing both parent classes properly using their explicit constructors
        Clock.__init__(self, time_zone)
        HealthTracker.__init__(self, target_steps)
        self.brand = brand

    def get_dashboard(self):
        return f"--- {self.brand} Smartwatch Dashboard ---"
    
# --- Real-Time Execution ---
my_device = SmartWatch(brand="FitBit Pro", time_zone="EST", target_steps=12000)

print(my_device.get_dashboard())
print(my_device.show_time())          # Inherited from Clock
print(my_device.track_heart_rate())    # Inherited from HealthTracker
# ==========================================
# METHOD OVERRIDING
# ==========================================

# child class changes parent method

class Parent():

    def show(self):
        print("Parent Method")


class Child(Parent):

    # overriding parent method
    def show(self):
        print("Child Method")


obj = Child()

obj.show()


# Output:
# Child Method


# ==========================================
# SUPER KEYWORD
# ==========================================

# super() is used to call parent class constructor/method

class Parent():

    def __init__(self):

        print("Parent Constructor")


class Child(Parent):

    def __init__(self):

        # calling parent constructor
        super().__init__()

        print("Child Constructor")


obj = Child()


# Output:
# Parent Constructor
# Child Constructor

# ==========================================
# METHOD OVERLOADING
# ==========================================

# Method Overloading = same method name
# with different number of arguments

# Python does not support true method overloading
# like Java. We achieve it using default arguments
# or *args

class Calculator():

    def add(self, a=0, b=0, c=0):
        print(a + b + c)


obj = Calculator()

obj.add(10, 20)
obj.add(10, 20, 30)

# Output:
# 30
# 60


# using *args

class Sum():

    def add(self, *numbers):
        print(sum(numbers))


obj = Sum()

obj.add(10, 20)
obj.add(10, 20, 30)
obj.add(10, 20, 30, 40)

# Output:
# 30
# 60
# 100


# ==========================================
# ENCAPSULATION
# ==========================================

# Encapsulation = binding variables and methods
# into single class and restricting direct access

# public variable -> normal variable
# protected variable -> _variable
# private variable -> __variable

class Employee():

    def __init__(self):
        self.name = "Bharat"        # public
        self._salary = 50000        # protected
        self.__bonus = 10000        # private

    def show(self):
        print(self.name)
        print(self._salary)
        print(self.__bonus)


obj = Employee()

print(obj.name)

print(obj._salary)

# print(obj.__bonus)  # error because private variable

obj.show()

# Output:
# Bharat
# 50000
# Bharat
# 50000
# 10000


# accessing private variable using method

class Bank():

    def __init__(self):
        self.__balance = 10000

    def get_balance(self):
        print(self.__balance)


obj = Bank()

obj.get_balance()

# print(obj.__balance) -> error


# ==========================================
# ABSTRACTION
# ==========================================

# Abstraction = hiding implementation details
# and showing only essential functionality

# using abstract class

from abc import ABC, abstractmethod


# abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# child class
class Car(Vehicle):

    def start(self):
        print("Car starts with key")


class Bike(Vehicle):

    def start(self):
        print("Bike starts with self start")


obj1 = Car()
obj2 = Bike()

obj1.start()
obj2.start()

# Output:
# Car starts with key
# Bike starts with self start


# if child class does not define abstract method
# object cannot be created


# ==========================================
# POLYMORPHISM
# ==========================================

# Polymorphism = one method behaves differently
# for different objects


# Example 1 : method overriding

class Animal():

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


obj1 = Dog()
obj2 = Cat()

obj1.sound()
obj2.sound()

# Output:
# Dog barks
# Cat meows


# Example 2 : same function works with different objects

class Car():

    def speed(self):
        print("Car speed is 120 km/h")


class Bike():

    def speed(self):
        print("Bike speed is 80 km/h")


def vehicle_info(vehicle):
    vehicle.speed()


c = Car()
b = Bike()

vehicle_info(c)
vehicle_info(b)

# Output:
# Car speed is 120 km/h
# Bike speed is 80 km/h


# ==========================================
# FINAL OOPS CONCEPTS
# ==========================================

# Inheritance     -> acquiring properties from parent class
# Encapsulation   -> hiding data and restricting access
# Polymorphism    -> same method different behavior
# Abstraction     -> hiding implementation details
# Overloading     -> same method with different arguments
# Overriding      -> child class changes parent method