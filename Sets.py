a= {1, 2, 2, 3, 4, 5}
if 1 in a:
    print("1 is present in the set a")  # prints "1 is present in the set a" because 1 is present in the set a  
    
myset = {1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10}
print(myset)  # prints the myset
print(type(myset))  # prints the type of myset
# set remove duplicate automatically and it is unordered collection of items. It is mutable means we can change the value of the set once it is created. If we want to change the value of the set then we can change the value of the set by using the add() method.

# if I wanted to perform union
b = {5, 6, 7, 8, 9, 10}
print(set_a.union(b))
# union meaning 
# intersection 
c = {6, 7, 8, 9}

#intersection means only those element which are common on both
print(b.intersection(c))

# remove the set item
set_a.remove(2)
print(set_a)
