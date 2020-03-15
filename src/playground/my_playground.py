#!/usr/bin/env python3
# encoding= utf-8

""" This is the playground to play around with python concepts

"""


class Snake:
            name = "python"

            def __init__(self, name):
                self.name = name

            def change_name(self, new_name): # note that the first argument is self
                self.name = new_name # access the class attribute with the self keyword



# Instantiate the class
snake = Snake()
# print the current object name 
#print(snake.name)


# Change the name using the change_name method
#snake.change_name("anaconda")
print(snake.name)
