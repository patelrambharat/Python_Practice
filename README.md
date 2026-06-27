# Python Practice Repository

This repository contains my Python learning and practice programs covering core Python concepts, functions, exception handling, OOP concepts, and advanced Python topics.

---

# 1. Variables and Data Types

Variables are used to store data.

```python
name = "Bharat"
age = 25
salary = 50000.50
is_active = True
```

Data Types:

- int  
- float  
- string  
- boolean  
- list  
- tuple  
- dictionary  

---

# 2. Conditional Statements

Used for decision making.

```python
x = 10

if x > 5:
    print("Greater")

else:
    print("Smaller")
```

---

# 3. Loops

### For Loop

```python
for i in range(5):
    print(i)
```

### While Loop

```python
x = 1

while x <= 5:
    print(x)
    x += 1
```

---

# 4. Functions

Reusable block of code.

```python
def greet():
    print("Hello")

greet()
```

Function with return:

```python
def add(a,b):
    return a+b
```

Default argument:

```python
def sum(a,b=10):
    return a+b
```

---

# 5. *args and **kwargs

### *args → multiple values (Tuple)

```python
def demo(*a):
    print(a)

demo(1,2,3)
```

### **kwargs → named arguments (Dictionary)

```python
def demo(**x):
    print(x)

demo(a=10,b=20)
```

---

# 6. Lambda Function

Anonymous one-line function.

```python
add = lambda a,b : a+b
print(add(2,3))
```

Square:

```python
square = lambda x : x*x
```

---

# 7. Map Function

Applies operation on every element.

```python
nums = [1,2,3]

print(list(map(lambda x:x*x, nums)))
```

Output:

```python
[1,4,9]
```

---

# 8. Filter Function

Filters values based on condition.

```python
nums = [1,2,3,4]

print(list(filter(lambda x:x%2==0, nums)))
```

Output:

```python
[2,4]
```

---

# 9. Reduce Function

Reduces list into one value.

```python
from functools import reduce

nums = [1,2,3,4]

print(reduce(lambda x,y:x+y, nums))
```

Output:

```python
10
```

---

# 10. Exception Handling

Used to handle runtime errors.

```python
try:
    a = 10/0

except Exception as e:
    print(e)
```

Finally block:

```python
try:
    a = 10/0

finally:
    print("Always runs")
```

Custom exception:

```python
age = -1

if age < 0:
    raise Exception("Invalid age")
```

---

# 11. String Formatting (f-string)

Insert variable inside string.

```python
name = "Bharat"

print(f"My name is {name}")
```

---

# 12. Global Variable

Variable declared outside function.

```python
count = 5

def update():
    global count
    count += 1
```

---

# 13. Enumerate

Returns index and value together.

```python
nums = [100,200,300]

for i,x in enumerate(nums):
    print(i,x)
```

Output:

```python
0 100
1 200
2 300
```

---

# 14. OOPS (Object Oriented Programming)

Class = Blueprint  
Object = Real instance

```python
class Employee:

    name = "Bharat"

obj = Employee()

print(obj.name)
```

---

# 15. Methods

Function inside class = Method

```python
class Employee:

    def info(self):
        print("Hello")
```

`self` refers to current object.

---

# 16. Constructor

Runs automatically when object is created.

```python
class Employee:

    def __init__(self):
        print("Constructor called")
```

Parameterized constructor:

```python
class Employee:

    def __init__(self,name):
        self.name = name
```

---

# 17. Attributes

### Class Attribute

Shared by all objects.

```python
class Employee:

    company = "Accenture"
```

### Instance Attribute

Unique for each object.

```python
class Employee:

    def __init__(self,name):
        self.name = name
```

---

# 18. Static Method

No self, no cls.

```python
class Employee:

    @staticmethod
    def add(a,b):
        return a+b
```

---

# 19. Class Method

Uses cls and class variables.

```python
class Employee:

    bonus = 10

    @classmethod
    def add(cls,a,b):
        return a+b+cls.bonus
```

---

# 20. Getter and Setter

Used for Encapsulation.

```python
class Employee:

    def __init__(self):
        self.__salary = 5000

    def getSalary(self):
        return self.__salary

    def setSalary(self,salary):
        self.__salary = salary
```

---

# Topics Covered

- Variables and Data Types  
- Conditional Statements  
- Loops  
- Functions  
- Default Arguments  
- *args and **kwargs  
- Lambda Functions  
- Map, Filter, Reduce  
- Exception Handling  
- String Formatting  
- Global Variables  
- Enumerate  
- OOPS  
- Methods  
- Constructor  
- Attributes  
- Static Method  
- Class Method  
- Getter and Setter  

---

# Tools Used

- Python 3  
- VS Code  
- Git  
- GitHub  

---

# Author

**Rambharat Patel**

GitHub: https://github.com/patelrambharat
