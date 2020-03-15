#!/usr/bin/env python3
# encoding= utf-8

"""
Python Modules

Module is nothing but a code library.

A file containing a set of functions you want to include in your application.

"""

import sys
sys.path.append('/src/module_and_package/module')
import arithmetic
print(arithmetic.add(1,2))


# Create an alias when you import a module,by using the as keyword: 
import arithmetic as ao
print(ao.sub(5,2))


# Import a method from a module
from arithmetic import add
print(add(1,8))

"""
# Standard library imports
import datetime
import osh

# Third party imports
from flask import Flask

# Local application imports
from local_module import local_class
from local_package import local_function

"""

# .pyc: This is the compiled bytecode. If you import a module, python will build a *.pyc file
# that contains the bytecode to make importing it again later easier (and faster).

"""
Python Module and Package

Module is a single file (or files) that are imported under one import and used.

#import arithmetic

Package is a collection of modules in directories that give a package hierarchy.

#from my_package.timing.internets import function_name_x

"""


"""
Python PIP

PIP is a package manager for Python packages, or modules.

It will download the packages or modules from the following repository.

https://pypi.org

# To see the PIP version
# pip --version

# To download and install package
# pip install <packageName>

# To uninstall the package
# pip uninstall <packageName>

# To List the all installed package in the system
# pip list

"""

