#!/usr/bin/env python3
# encoding= utf-8

"""
Python String

Strings are sequences of characters.

To create a string, put the sequence of characters inside either single quotes, 
double quotes, or triple quotes and then assign it to a variable.
"""

# Create a string and assign it to a variable
single_quote_character = 'a'
print(single_quote_character)
print(type(single_quote_character)) 

double_quote_character = "b"
print(double_quote_character)
print(type(double_quote_character))

double_quote_multiple_characters = "aeiou"
single_quote_multiple_characters = 'aeiou'
print(type(double_quote_multiple_characters), type(single_quote_multiple_characters))

# Check the equivalence of one to the other using the keyword "is"
print(double_quote_multiple_characters is double_quote_multiple_characters)

# Multiple lines are generally put in triple quotes.
# You can use single and double quotes for a single line of characters.
triple_quote_example = """this is a sentence written in triple quotes"""
print(triple_quote_example)




# String common methods

# Get the index of a substring in a string
# Find the index of a "c" in a string "abcde"
"abcde".index("c")

# Test if string "o" is present in string "python" at least once. It return true / false
"o" in "python"

# Join a list of strings 1, 2, 3 with a space as a delimiter and 1,2,3 as the list of strings.
combined_string = " ".join(["1", "2", "3"])
print(combined_string)

# Split the string "1 2 3" and return a list of the numbers.
split_string = "1 2 3".split() 
print(split_string)

# Split a string based on a delimiter like :.
split_using_delimiter = "1:2:3".split(":")
print(split_using_delimiter)

# Formatting in String
# String object can be formatted. 
# You can use %s as a formatter which will enable you to insert different values into a string
print("I love %s in %s" % ("programming", "Python")) # templating strings

# Using the keyword format. This will enable you to set your own formatters instead of %s.
print("I love {programming} in {python}".format(programming="programming", python="Python"))

