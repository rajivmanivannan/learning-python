#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
#!/usr/bin/python3 is a shebang line

A shebang / hash bang  line defines where the interpreter is located.

#!/usr/bin/python: writing the absolute path

#!/usr/bin/env python: using the operating system env command, 
which locates and executes Python by searching the PATH environment variable
"""


"""
Python Variables

Variables are used to store information to be referenced and manipulated in a computer program.

Assignment can be done by writing the variable name followed by the value separated by an equal = symbol.
"""

# Assign the value 2812 to the variable date_of_birth
date_of_birth = 2812
print(date_of_birth)

# Assign a decimal number 1.3 oz to the variable weight_of_donut
weight_of_donut = 1.3
print(weight_of_donut)

# assign a string
fav_donut_shop = "Krispy Kreme"
print(fav_donut_shop)

# you can have variable name in your local language as well.
చెప్పు ='Tell me' 
print(చెప్పు)

வணக்கம் = 'Hello'
print(வணக்கம்)


# Python supports assigning all data structures to variables.
# built-in data structures like lists,dictionary etc.,

# Assign a list to a variable
types_of_donut = ['Chocolate Frosted','Cinnamon Twist','Strawberry Frosted','Blueberry']
print(types_of_donut)

# Assign a dicts to a variable
donut_prices = {"Chocolate Frosted": 30, "Cinnamon Twist": 40, "Strawberry Frosted":60, "Blueberry":60}
print(donut_prices)

# Assign function to variable
import platform
this_platform = platform.platform()
print(this_platform)

# Assign classes to variable
class DonutShop: 
    # Constructor
    def __init__(self, shop_name = ""): 
        self._shop_name = shop_name 
    # getter method 
    def get_shop_name(self): 
        return self._shop_name 
    # setter method 
    def set_shop_name(self, new_shop_name): 
        self._price = new_shop_name

donut_price = DonutShop('Krispy Kreme')
print(donut_price)
