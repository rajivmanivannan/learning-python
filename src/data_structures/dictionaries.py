#!/usr/bin/env python3
# encoding= utf-8

"""
Python Dictionaries

A dictionary is a set of unordered key, value pairs. 
In a dictionary, the keys must be unique and they are stored in an unordered manner.

Dictionary is separate the key-value pairs by a colon(“:”). 
The keys would need to be of an immutable type.
i.e., data-types for which the keys cannot be changed at runtime such as int, string, tuple, etc. 

The values can be of any type. Individual pairs will be separated by a comma(“,”) 
and the whole thing will be enclosed in curly braces({...}).
"""

# Create a Dictionay
person_information = {'name': 'John', 'city': 'San Francisco'}
type(person_information)
print(person_information)

# Get value from Dictionay
print(person_information["city"])
print(person_information.get("city"))

# Get the value with key company. Pass “default” as default. 
# Since key company does not exist, you get “default” as the return value.
print(person_information.get("company", "default"))

# update the key, value information with key company
person_information["company"] = "Google"

# Delete a element from the dictonary
del person_information["company"]

# To check the presence of key 
person_information

# Loop
for k, v in person_information.items():
        print("key is: %s" % k)
        print("value is: %s" % v)
