#!/usr/bin/env python3
# encoding= utf-8

"""
Python Internals

Python is an interpreted object-oriented programming language. 
By interpreted it is meant that each time a program is run the interpreter checks through the code
for errors and then interprets the instructions into machine-readable bytecode.

An interpreter is a translator in computer's language which translates the given code line-by-line in machine readable bytecodes.
And if any error is encounterd it stops the translation until the error is fixed. 
Unlike C language, which is a compiled programming language.  

The compiler translates the whole code in one-go rather than line-by-line. 
This is the reason why in C language, all the errors are listed during compilation only.

"""

"""
The Python interpreter performs following tasks to execute a Python program :

Step 1 : The interpreter reads a python code or instruction.Then it verifies that the instruction is well formatted, i.e.
it checks the syntax of each line.If it encounters any error, it immediately halts the translation and shows an error message.

Step 2 : If there is no error, i.e. if the python instruction or code is well formatted then the interpreter translates
it into its equivalent form in intermediate language called “Byte code”.The .pyc files you see are byte code for the 
Python virtual machine.After successful execution of Python script or code, it is completely translated into Byte code.

Step 3 : Byte code is sent to the Python Virtual Machine(PVM).Here again the byte code is executed on PVM.
If an error occurs during this execution then the execution is halted with an error message.

"""


"""
Interpreters and compilers are very similar in structure. 

The main difference is that an interpreter directly executes the instructions in the source programming language
while a compiler translates those instructions into efficient machine code.


Compiler Language

- Takes entire program as single input and converts it into object code which is stored in the file.
- Intermediate Object code is generated e.g: C,C++
- Compiled programs run faster because compilation is done before execution.
- Memory requirement is more due to the creation of object code.
- Error are displayed after the entire program is compiled
- Source code ---Compiler ---Machine Code ---Output

Interpreter Language:

Takes single instruction as single input and executes instructions.
Intermediate Object code is NOT generated e.g: Python,Perl
Interpreted programs run slower because compilation and execution take place simultaneously.
Memory requirement is less.
Error are displayed for every single instruction.
Source Code ---Interpreter ---Output

"""

"""
In Python’s interactive interpreter, we can invoke the built-in function: 
compile, and get the code object of this module.

> python3
> c = compile(open('test.py').read(), 'test.py', 'exec')
> c.co_code

In Python’s standard library there’s a module called dis, which would translate the byte codes for us.

To disassemble the Python module, run 
> python3 -m dis test.py

Python virtual machine is a “Stack Machine.” Python internally keeps track of a “Value Stack,” 
which stores all the values for the upcoming operations to use.

"""