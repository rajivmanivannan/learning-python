#!/usr/bin/env python3
# encoding= utf-8

"""
Functions

A function is a block of code that takes in some data and, either performs some kind of transformation
and returns the transformed data, or performs some task on the data, or both. 

Functions are useful because they provide a high degree of modularity. 
Similar code can be easily grouped into functions and you can provide a name to the function
that describes what the function is for.
"""

"""
def name_of_the_function(arguments):
    '''
    doctring of the function
    note that the function block is indented by 4 spaces
    '''
    body of the function
    return the return value or expression
"""    

def add_two_numbers(num1, num2):
    '''
    Summary line... 
    Extended description of function. 
    Parameters: 
    arg1 (int): Description of arg1 
    arg2 ...
    Returns: 
    int: Description of return value
    '''
    result = num1 + num2
    return result

result = add_two_numbers(1, 2)
print(result)

"""
Keyword def: This is the keyword used to say that a function will be defined now,
and the next word that is there, is the function name.

Function name: This is the name that is used to identify the function. 
The function name comes after the def keyword. 
Function names have to be a single word. 
PEP8, which is a style guide for Python, recommends that in case multiple words are used, 
they should be in lowercase and they should be separated with an underscore. 
In the example above, add_two_numbers is the parameter name.

Parameter list: Parameter list are place holders that define the parameters 
that go into the function.The parameters help to generalise the transformation/computation/task
that is needed to be done. 
In Python, parameters are enclosed in parentheses.
In the example above, the parameters are num1and num2. 
You can pass as many parameters as needed to a function.

Function docstrings: These are optional constructs that provide a convenient way 
for associated documentation to the corresponding function. 
Docstrings are enclosed by triple quotes '''you will write the docstring here'''

Function returns: Python functions returns a value. 
You can define what to return by the return keyword. 
In the example above, the function returns result. 
In case you do not define a return value, the function will return None.
"""

# Call a function that performs a task and has no return value

def printing_side_effects():
    '''a function with side effects'''
    print('this is a function with side effects and performs some task')

printing_side_effects()