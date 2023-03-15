# A module in Python is simply a file that contains Python definitions and statements. Modules can define functions, classes,
# and variables, and can be imported into other Python scripts to be used in that script. Modules are an important
# aspect of Python programming as they allow for code reuse, which saves time and makes the code more maintainable.

# To use a module in your Python script, you first need to import it. You can do this using the import statement,
# followed by the name of the module. For example:
import math
# This will import the math module, which provides mathematical functions like sqrt() and sin().

# You can also import specific functions or variables from a module using the from keyword. For example:
from math import sqrt, pi
# This will import the sqrt() and pi variables from the math module, allowing you to use them directly in your
# script without needing to prefix them with the module name.

# It's worth noting that you can also create your own modules in Python by simply writing Python code and saving
# it as a .py file. Once you've done this, you can import your module into other Python scripts just like you would any other module.

# That's a brief introduction to Python modules. Modules are an important concept in Python programming, so it's
# worth taking the time to understand how they work and how to use them effectively.

# Here are a few examples of how to use modules in Python:

# 1. Using the math module to perform mathematical calculations:
import math

# Calculate the square root of 2
print(math.sqrt(2))

# Calculate the value of pi
print(math.pi)

# Calculate the sine of 30 degrees
print(math.sin(math.radians(30)))

# 2. Using the random module to generate random numbers:
import random

# Generate a random integer between 1 and 10 (inclusive)
print(random.randint(1, 10))

# Generate a random floating-point number between 0 and 1
print(random.random())

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# 3. Creating and using your own module:
# Create a module called my_module.py in another file
# with a function called greeting()

def greeting(name):
    print("Hello, " + name + "!")

# Import the greeting function from my_module.py to your main file
# from my_module import greeting

# Call the greeting function
greeting("Alice")

# These are just a few examples of how you can use modules in Python. There are many other modules available that you can use
# to perform various tasks, so be sure to explore the Python standard library and third-party packages to see what's available