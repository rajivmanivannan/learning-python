#!/usr/bin/env python3
# encoding= utf-8

"""
To perform the calculation, programming language need to supports the number. 
Python provides support to numbers and are categorized into different data-types.
Eg: int for integers, float for decimal numbers, and complex for complex numbers.

Data A type is a way to define various data structures and containers and define 
the functionality associated with them. Types are implemented in Python as classes. 
If you want to verify if an integer belongs to the class int you can use isinstance().
"""

# Check the value 2 is integer or not. It return boolean response.
isinstance(2, int)

# We can use type() function to know the type of value that a variable holds.
a = 10
print(type(a))

# Arithmetic operations using numbers

# Assign the integer 5 to a var int_var_a
int_var_a = 5

# Assign the integer 2 to a var int_var_b
int_var_b = 2

# Print the sum of the two variables int_var_a and int_var_b
print(int_var_a + int_var_b)





# Arithmetic operations using Decimal numbers

# Assign a decimal number to a variable float_var_a
float_var_a = 5.6

# Assign another decimal number to a variable float_var_b
float_var_b = 6.7

# Print the sum of the two decimal numbers
print(float_var_a + float_var_b)




# Arithmetic operations using complex numbers

# Assign a complex number to a variable complex_var_a
complex_var_a = (1 + 2j)

# Assign another complex number to a variable complex_varb
complex_var_b = (2 + 3j)

# Print the sum of the two complex numbers
print(complex_var_a + complex_var_b)



#In case of division, dividing two integers will always result in a float.

# divide two integers and assign it to a variable result
result = 8/2
print(result)
print(isinstance(result, float))

