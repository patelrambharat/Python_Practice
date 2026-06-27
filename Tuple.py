# Tuple
# A tuple is an ordered, immutable collection of items defined with parentheses.
# Example: my_tuple = (1, 2, 3)

my_tuple = (1, 2, 3)  # define a tuple with three integers
print("Tuple:", my_tuple)  # print the whole tuple
print("First item:", my_tuple[0])  # print the first element of the tuple
print("Length:", len(my_tuple))  # print the number of items in the tuple

# Tuples support slicing and unpacking
first, second, third = my_tuple  # unpack tuple values into separate variables
print("Unpacked:", first, second, third)  # print the unpacked values
print("Slice:", my_tuple[1:])  # print a slice of the tuple from index 1 onward

# Single-element tuple requires a trailing comma
single_item_tuple = (42,)  # define a tuple with a single element using a trailing comma
print("Single item tuple:", single_item_tuple)  # print the single-element tuple

# Convert the tuple to a list to modify it
my_tuple_list = list(my_tuple)  # convert the original tuple to a list
my_tuple_list.append(6)  # append a new item to the list
print(my_tuple_list)  # print the modified list

# Convert back to a tuple if desired
my_tuple = tuple(my_tuple_list)  # convert the modified list back to a tuple
print("Modified tuple:", my_tuple)  # print the resulting tuple

