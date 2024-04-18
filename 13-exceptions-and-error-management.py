# In Python, exception handling allows you to handle errors and unexpected situations
# that may occur during the execution of your code. Errors can occur due to various reasons,
# such as invalid input, file not found, or division by zero. Exception handling helps prevent
# your program from crashing and allows you to handle errors gracefully.

# Try-Except Block
# The try-except block is used to catch and handle exceptions in Python. It allows you to
# specify code that may raise an exception and provide alternative code to
# execute if an exception occurs.

try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero")

# In the above example, if the division by zero occurs, the ZeroDivisionError
# exception is caught, and the error message is printed.

# Handling Multiple Exceptions
# You can handle multiple exceptions using multiple except blocks or a single
# except block with multiple exception types.

try:
    # Code that may raise exceptions
    result = int("abc")
except ValueError:
    # Code to handle ValueError
    print("Error: Invalid conversion")
except ZeroDivisionError:
    # Code to handle ZeroDivisionError
    print("Error: Division by zero")


# Finally Block
# The finally block is used to execute code regardless of whether an exception occurs or not.
# It is often used to perform cleanup actions, such as closing files or releasing resources.

try:
    # Code that may raise an exception
    file = open("example.txt", "r")
    data = file.read()
except FileNotFoundError:
    # Code to handle FileNotFoundError
    print("Error: File not found")
finally:
    # Code to execute regardless of exceptions
    if file:
        file.close()

# In the above example, the finally block ensures that the file is closed,
# whether an exception occurs or not.


# Conclusion
# Exception handling and error management are essential concepts in Python programming.
# They allow you to handle errors gracefully, prevent program crashes, and improve the
# reliability of your code. By using try-except blocks, finally blocks, and custom exceptions,
# you can effectively manage errors and handle unexpected situations in your code.