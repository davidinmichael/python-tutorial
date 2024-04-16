# In Python, a function is a block of reusable code that performs a specific task.
# Functions allow you to break down your program into smaller, manageable pieces, making
# your code more organized, readable, and reusable.

# Creating a Function
# You can create a function in Python using the def keyword followed by the function
# name and parentheses containing any parameters the function takes. The function body is
# indented below the def statement.
def greet(name):
    print(f"Hello, {name}!")

# Calling a Function
# To call a function, simply use the function name followed by parentheses and
# provide any necessary arguments.
greet("Alice")

# Returning Values
# Functions can also return values using the return statement. You can use the returned
# value in your code or assign it to a variable.
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# Default Parameters
# You can specify default values for parameters in a function. If a parameter is not provided
# when the function is called, it will use the default value.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!

# Keyword Arguments
# You can also use keyword arguments to specify the parameter values by their names,
# which allows you to pass arguments in any order.