#  list is a 1-D array
list1 = [1, 2, 3, 4, 5]
# give the definition of the list
# list is a collection of items which is ordered and changeable. It allows duplicate members. In python list is defined as a sequence of items enclosed in square brackets [].
# list is mutable means we can change the value of the list once it is created. If we want to change the value of the list then we can change the value of the list by using the index of the list.
print(list1)  # prints the list1
mylist = [1, 2, 3, "bharat", "patel", 0, "aa", True, False, 1.2, 2.3, 3.4]
print(mylist)  # prints the mylist

print(mylist[0])  # prints the first element of the mylist
print(mylist[0:3])  # prints the first three elements of the mylist
print(mylist[-3:])  # prints the third last element of the mylist
print(mylist[len(mylist)-3:len(mylist)])  # prints the third last element of the mylist
mylist[0] = "ram"  # changes the first element of the mylist to "ram"
print(mylist)  # prints the mylist after changing the first element to "ram"

print(mylist[0::2])  #jump two index
mylist.append("hero")
print(mylist) 
mylist.insert(1,"neha")
print(mylist)
mylist.remove("neha")
print(mylist)

# I wanted to reverse the list
mylist.reverse()
print(mylist)  # prints the mylist after reversing the list
print(mylist)  # prints the mylist after sorting the list

list2 = [1, 2, 3, 4, 5]
print(list2[::-1])  # prints the list2 in reverse order

# list comprehension -> it is a concise way to create a list in python. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
# list comprehension is used to create a new list from an existing list by applying an expression to
    #each element of the existing list. It is a more readable and concise way to create a new list than using a for loop.
new_list= []
for i in list2:
    new_list.append(i*i)  # appends the square of each element of the list2 to the new_list
print(new_list)

# using list comprehension
new_list2 = [i*i for i in list2]  # creates a new list by applying the expression i*i to each element of the list2
print(new_list2)  # prints the new_list2

# now I wanted to also check whether the number is even or odd and then I wanted to append the square of the even number to the new list
new_list3 = [i*i for i in list2 if i%2 == 0]  # creates a new list by applying the expression i*i to each even element of the list2
print(new_list3)  # prints the new_list3

# I wanted to add one more condition to check whether the number is greater than 2 or not and then I wanted to append the square of the even number to the new list

new_list4 = [i*i for i in list2 if i%2 == 0 and i>2]  # creates a new list by applying the expression i*i to each even element of the list2 which is greater than 2