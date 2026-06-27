# Dictionary
# Dictionary is very useful when we working on json
# key value pair
# dictionary is mutable means we can change the value of the dictionary once it is created. If we want to change the value of the dictionary then we can change the value of the dictionary by using the key of the dictionary.
my_dict = {"name": "bharat", "age": 25, "city": "ahmedabad"}
print(my_dict)  # prints the my_dict

my_dict["age"] = 26  # changes the value of the key "age" to 26
print(my_dict)  # prints the my_dict after changing the value of the key "age
# difference between list and dictionary is that list is ordered and dictionary is unordered. In list we can access the elements by using the index of the list but in dictionary we can access the elements by using the key of the dictionary.    
my_dict.pop("city")  # removes the key "city" from the my_dict
print(my_dict)  # prints the my_dict after removing the key "city"

print(my_dict.keys())  # prints the keys of the my_dict
print(my_dict.values())  # prints the values of the my_dict
print(my_dict.items())  # prints the key-value pairs of the my_dict

my_dict = {"name": "bharat", "age": 25, "city": "ahmedabad", "hobbies": ["reading", "writing", "coding"]}
print(my_dict)  # prints the my_dict
my_dict["hobbies"].append("playing")  # appends the value "playing" to the key "hobbies" in the my_dict
print(my_dict)  # prints the my_dict after appending the value "playing" to