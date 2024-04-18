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
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="dog", pet_name="Buddy")


# Variable Number of Arguments
# If you're not sure how many arguments a function will receive, you can use *args to handle a
# variable number of positional arguments or **kwargs for a variable number of keyword arguments.
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = add_all(1, 2, 3, 4, 5)
print(result)  # Output: 15


# Scope of Variables
# Variables defined inside a function are scoped to that function and are not accessible outside of it.
# You can use the global keyword to modify a global variable within a function.
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1


# Functions are a powerful feature in Python that help you write modular and reusable code.
# By breaking down your program into functions, you can improve readability, maintainability, and code organization.