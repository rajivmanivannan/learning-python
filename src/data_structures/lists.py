#!/usr/bin/env python3
# encoding= utf-8

"""
List

A list is a data-structure, or it can be considered a container that can be used to store multiple data at once.

The list will be ordered and there will be a definite count of it. 
The elements are indexed according to a sequence and the indexing is done with 0 as the first index.
Each element will have a distinct place in the sequence and if the same value occurs multiple times 
in the sequence, each will be considered separate and distinct element

Lists are great if you want to preserve the sequence of the data and then iterate over them later for various purposes. 
"""

# To create a list, you separate the elements with a comma and enclose them with a bracket “[]”
companies = ["Google", "Tesla"]

# get the first company name
print(companies[0])

# get the second company name
print(companies[1])

# Two-dimensional list

companies = [["Google", "Tesla"],["Zoho", "Freshworks"]]

print(companies[0][1])


# Python lists support common methods that are commonly required while working with lists.

# Create an empty list
companies = []

# Add "Google" to companies
companies.append("Google")

# Add "Facebook" to companies
companies.append("Facebook")
print(companies)

# Insert “airbnb” at position 2
companies.insert(2, "Airbnb")
print(companies)

# To add another list
companies.extend(["Zoho", "Freshworks"])
print(companies)


# To find out the index of value
companies.index("Zoho")
print(companies)

#To remove a element from list
companies.remove("Airbnb")
print(companies)
