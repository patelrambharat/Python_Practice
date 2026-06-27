# loops -> perform iterations
# for loop -> used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.

for i in range(5):
    print(i, end=" ")  # prints the value of i from 0 to 4
# now in the next line I wanted to print the value of i from 0 to 4

my_list = ["orders", "customers", "products"]
for i in my_list:
    print(i, end=" ")  # prints the value of i from my_list
    
tbl_list = ["orders", "customers", "products"]
for i in tbl_list:
    if(i == "customers"):
        print("\nI found the table customers")  # prints "I found the table customers" if i is equal to "customers"
         
    elif(i == "products"):
        print("\nI found the table products")  # prints "I found the table products" if i is equal to "products"
        
    else:
        print("\nI did not find the table")  # prints "I did not find the table" if i is not equal to "customers" or "products" 
        
    
# let me print the start pattern
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")  # prints the star pattern
    print("\n")  # prints a new line after each row of stars
# let me print the star pattern in reverse order
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")  # prints the star pattern in reverse order
    print("\n")  # prints a new line after each row of stars
    
# break and continue statement
# break statement is used to terminate the loop when a certain condition is met. It will break the loop and exit from it.

# continue statement is used to skip the current iteration of the loop when a certain condition is met. It will skip the current iteration and move to the next iteration of the loop.

for i in tbl_list:
    if(i == "customers"):
        print("\nI found the table customers")  # prints "I found the table customers" if i is equal to "customers"
        break  # breaks the loop when i is equal to "customers"
    else:
        print("\nI did not find the table")  # prints "I did not find the table" if i is not equal to "customers"
        
# now I wanted to use the continue statement
for i in tbl_list:
    if(i == "customers"):
        print("\nI found the table customers")  # prints "I found the table customers" if i is equal to "customers"
        continue  # skips the current iteration when i is equal to "customers"
    else:
        print("\nI did not find the table")  # prints "I did not find the table" if i is not equal to "customers"
        
# while loop -> used to iterate over a block of code as long as the condition is true. It will keep executing the block of code until the condition becomes false.

i = 0
while(i < 5):
    print(i, end=" ")  # prints the value of i from 0 to 4
    i += 1  # increments the value of i by 1
print("\n")  # prints a new line after the while loop 
# do while loop -> used to iterate over a block of code at least once and then it will check the condition. It will keep executing the block of code until the condition becomes false.

# difference between while loop and do while loop is that while loop will check the condition first and then it will execute the block of code, whereas do while loop will execute the block of code first and then it will check the condition.

# give the 90 degree rotation code using python for array for 2*2 
arr = [[1, 2], [3, 4]]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[j][i], end=" ")  # prints the 90 degree rotation of the array
    print("\n")  # prints a new line after each row of the rotated array
# can we do the same with O(n) without nested loop and without zip function
print("90 degree rotation of the array without nested loop and without zip function")
for i in range(len(arr)):
    print(arr[0][i], arr[1][i])  # prints the 90 degree rotation of the array without nested loop and without zip function