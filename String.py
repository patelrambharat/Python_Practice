x = "bharat"
# definition of the string 
# String is a sequence of characters. It is used to store text data. In python string is defined as a sequence of characters enclosed in single quotes or double quotes.
# String is immutable means we cannot change the value of the string once it is created. If we want to change the value of the string then we need to create a new string with the new value.
# print this text as array
# print the first character of the string
print(x[0])  # prints the first character of the string x
print(x[1])  # prints the second character of the string x
for i in x:
    print(i)  # prints each character of the string x
# now I wanted to print in the same line
print("printing in the same line")
for i in x:
    print(i, end="")  # prints each character of the string x in the same line

# slicing in the string 
print("\nSlicing in the string")
print(x[1:4])  # prints the substring of the string x from index 1 to 3
print(x[:4])   # prints the substring of the string x from the beginning to index 3
print(x[1:])   # prints the substring of the string x from index 1 to the end
# if we do not specify anything
print(x[:])  # prints the whole string x it will print till n 
print(x[0:len(x)])  # prints the whole string x it will print till n

# string methods
print("\nString methods")

x = "bharat patel"
print(x.upper())  # converts the string x to uppercase
print(x.lower())  # converts the string x to lowercase
print(x.capitalize())  # converts the first character of the string x to uppercase 
print(x.title())  # converts the first character of each word in the string x to uppercase

print(x.split())  # splits the string x into a list of words
print(x.join(['hello', 'world']))  # joins the elements of the list with the string x as the separator
print(x.replace("bharat", "ram"))  # replaces the substring "bharat" with "ram" in the string x
print(x.find("patel"))  # returns the index of the first occurrence of the substring "patel" in the string x
print(x.count("a"))  # returns the number of occurrences of the substring "a" in the string x
print(x.replace("bh", "ram"))  # replaces the substring "bh" with "ram" in the string x

# List in String
x = "Bharat patel Love python "
print(x.split())  # splits the string x into a list of words
x = "raw_data.csv"
# we need to only read the file if it is csv file
if x.endswith(".csv"):
    print("This is a csv file")
if(x.startswith("raw")):
    print("This is a raw data file")
    
statement = "Hey bharat what are you doing. I am doing good. I am learning python."
print(statement.split('.'))  # splits the string statement into a list of sentences
print(statement.count('.'))  # returns the number of occurrences of the substring "." in the string statement

# is function is used to check whether the string is alphanumeric or not. It returns True if the string is alphanumeric, otherwise it returns False.

demo_str  = "hello"
print(demo_str.isalnum())  # returns True because the string demo_str is alphanumeric
print(demo_str.isdecimal())  # returns False because the string demo_str is not decimal
print(demo_str.isdigit())  # returns False because the string demo_str is not digit