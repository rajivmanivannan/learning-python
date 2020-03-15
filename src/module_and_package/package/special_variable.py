

"""
Special Variables

When the Python interpeter reads a source file, it first defines a few special variables.
In this case, we care about the __name__ variable.

The global variable, __name__, in the module that is the entry point to your program,
is '__main__'. Otherwise, it's the name you import the module by.

So,code under the if block will only run if the module is the entry point to your program.

It allows the code in the module to be importable by other modules, without executing the code block beneath on import.

"""
if __name__ == '__main__':
    print("Special Variables")

"""
Running Modules With the -m Option

The -m option searches sys.path for the module name and runs its content as __main__:
"""