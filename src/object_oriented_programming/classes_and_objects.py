#!/usr/bin/env python3
# encoding= utf-8

"""
Python Classes and Methods

Python is an “object-oriented programming language.”
This means that almost all the code is implemented using a special construct called classes.
Programmers use classes to keep related things together. 
This is done using the keyword “class,” which is a grouping of object-oriented constructs.

"""


"""
What is a class?

A class is a code template for creating objects. Objects have member variables and have behaviour 
associated with them. In python a class is created by the keyword class.

An object is created using the constructor of the class. 
This object will then be called the instance of the class. 
In Python we create instances in the following manner

Instance = class(arguments)
"""

class Snake:

            pass

snake = Snake()
print(snake)

"""
Attributes and Methods in class:

A class by itself is of no use unless there is some functionality associated with it. 
Functionalities are defined by setting attributes, which act as containers for data and 
functions related to those attributes. Those functions are called methods.
"""

class Snake:
    name = "python" # set an attribute `name` of the class

# Instantiate the class Snake and assign it to variable snake
snake = Snake()

# Access the class attribute name inside the class Snake.
print(snake.name)

"""
Methods

Once there are attributes that “belong” to the class, 
you can define functions that will access the class attribute. 
These functions are called methods. When you define methods, 
you will need to always provide the first argument to the method with a self keyword.

"""

class Snake:
            name = "python"

            def change_name(self, new_name): # note that the first argument is self
                self.name = new_name # access the class attribute with the self keyword



# Instantiate the class
snake = Snake()
# print the current object name 
print(snake.name)


# Change the name using the change_name method
snake.change_name("anaconda")
print(snake.name)

"""
Instance attributes in python and the init method

You can also provide the values for the attributes at runtime. 
This is done by defining the attributes inside the init method.
"""

class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

# two variables are instantiated
python = Snake("python")
anaconda = Snake("anaconda")

# print the names of the two variables
print(python.name)
print(anaconda.name)
