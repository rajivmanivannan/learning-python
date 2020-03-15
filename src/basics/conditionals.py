#!/usr/bin/env python3
# encoding= utf-8

"""
Python Control Structures - Loops and Conditionals

You can control the flow of logic in your code through various methods.

Basic control flows

1.Selection (if statements)
2.Iteration (for loops)

To have sequential, selective and iterative flows in your code. 
This can be achieved using the for loop.
"""


"""
Selection and Python If statements

As a programmer, you will continually feel the need to control the flow of your 
program and let it make runtime decisions based on some condition. 
The is done using the if syntax. 
To implement this you can look at the if .. elif .. else syntax.

if condition1:
        code_block1
elif condition2:
        code_block2
else:
        code_block3
"""

num = 44
if num == 42:
    print("number is 42")
elif num == 44:
    print("num is 44")
else:
    print("num is neither 42 nor 44")


# Nested if statements

num = 42
if num > 20:
    if num < 50:
        print("num between 20 and 50")

        
"""
Loops
Working on items of the iterable
If you want to run an operation on a collection of items, then you can do it using "for" loops. 
for statement line will end with a colon : and the rest of the code block 
must be indented with a spacing of 4 spaces. 

for item in iterable: # you can place any list or tuple or string in place of iterable
    # write your code here.
    pass
"""

fruits = ["apples", "oranges", "mangoes"]
for fruit in fruits:
    print(fruit)

"""
Looping on both indexes and items
if you are interested in working with the index, 
then you can call the enumerate function which returns a tuple of the index and the item. 
"""    

fruits = ["apples", "oranges", "mangoes"]
for index, fruit in enumerate(fruits):
    print("index is %s" % index)
    print("fruit is %s" % fruit)

"""
While statement

The while statement will execute a block of code as long as the condition is true. 

while condition:
    code_block
"""

fruits = ["apples", "oranges", "mangoes"] # get the list
length = len(fruits) # get the length that will be needed for the while condition
i = 0 # initialise a counter
while i < length: # give the condition
    print(fruits[i]) # the code block
    i += 1 # increment the counter