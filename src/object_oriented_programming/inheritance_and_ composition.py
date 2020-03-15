#!/usr/bin/env python3
# encoding= utf-8

"""
Classes are written to organize and structure code into meaningful blocks, which can then be used to implement the business logic.

These implementations are used in such a way that more complex parts are abstracted away to provide for simpler interfaces which can 
then be used to build even simpler blocks. While doing this we will find that there are lots of times when we will need 
to establish relationships between the classes that we build. 

These relationships can then be established using either

1.inheritance  
2.composition.

"""


"""
Python inheritance

In inheritance an object is based on another object. When inheritance is implemented, the methods and attributes 
that were defined in the base class will also be present in the inherited class. 

This is generally done to abstract away similar code in multiple classes. 

The abstracted code will reside in the base class and the previous classes will now inherit from the base class.

Python allows the classes to inherit commonly used attributes and methods from other classes through inheritance.

class DerivedClassName(BaseClassName):
    pass
"""

class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)


class MarsRover(Rocket): # inheriting from the base class
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.name, self.maker)


if __name__ == "__main__":
    x = Rocket("Simple rocket", "till stratosphere")
    y = MarsRover("Mars rover", "till Mars", "ISRO")
    print(x.launch())
    print(y.launch())
    print(y.get_maker()) 


"""
Python Composition

In composition, we do not inherit from the base class but establish relationships between classes 
through the use of instance variables that are references to other objects.

class GenericClass:
    define some attributes and methods

class ASpecificClass:
    Instance_variable_of_generic_class = GenericClass

# use this instance somewhere in the class
    some_method(Instance_variable_of_generic_class)

"""

class MarsRoverComp():
    def __init__(self, name, distance, maker):
        self.rocket = Rocket(name, distance) # instantiating the base

        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.rocket.name, self.maker)


if __name__ == "__main__":
    z = MarsRover("mars_rover2", "till Mars", "ISRO")
    print(z.launch())
    print(z.get_maker())