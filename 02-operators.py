# Operators
# Operators are special symbols in Python that are used to perform operations on variables and values. Python has a variety of operators that you can use to perform arithmetic, comparison, logical, and bitwise operations.

# Arithmetic Operators
# Arithmetic operators are used to perform mathematical operations on numeric values. Python supports the following arithmetic operators:

# + Addition: Adds two operands
# - Subtraction: Subtracts the second operand from the first operand
# * Multiplication: Multiplies two operands
# / Division: Divides the first operand by the second operand
# % Modulus: Returns the remainder when the first operand is divided by the second operand
# ** Exponentiation: Raises the first operand to the power of the second operand
# // Floor division: Divides the first operand by the second operand and rounds down to the nearest integer
# Here's an example that demonstrates how to use arithmetic operators in Python:
x = 10
y = 3

print(x + y)  # Output: 13
print(x - y)  # Output: 7
print(x * y)  # Output: 30
print(x / y)  # Output: 3.3333333333333335
print(x % y)  # Output: 1
print(x ** y)  # Output: 1000
print(x // y)  # Output: 3

# Comparison Operators
# Comparison operators are used to compare values and return a Boolean value (True or False). Python supports the following comparison operators:

# == Equal to: Returns True if the two operands are equal
# != Not equal to: Returns True if the two operands are not equal
# > Greater than: Returns True if the first operand is greater than the second operand
# < Less than: Returns True if the first operand is less than the second operand
# >= Greater than or equal to: Returns True if the first operand is greater than or equal to the second operand
# <= Less than or equal to: Returns True if the first operand is less than or equal to the second operand
# Here's an example that demonstrates how to use comparison operators in Python:
x = 10
y = 3

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)  # Output: True
print(x < y)  # Output: False
print(x >= y)  # Output: True
print(x <= y)  # Output: False

# Logical Operators
# Logical operators are used to combine conditional statements and return a Boolean value. Python supports the following logical operators:

# and Logical AND: Returns True if both operands are True
# or Logical OR: Returns True if at least one of the operands is True
# not Logical NOT: Returns the opposite of the operand's Boolean value
# Here's an example that demonstrates how to use logical operators in Python:
x = 5
y = 10
z = 15

# Logical AND (returns True only if both conditions are True)
print(x < y and y < z)  # Output: True
print(x < y and z < y)  # Output: False

# Logical OR (returns True if at least one condition is True)
print(x < y or y < z)   # Output: True
print(x < y or z < y)   # Output: True
print(x > y or z < y)   # Output: False

# Logical NOT (inverts the Boolean value of a condition)
print(not x < y)        # Output: False
print(not x > y)        # Output: True

# Assignment Operators
# Assignment operators are used to assign values to variables. Here are the most commonly used assignment operators in Python:

# Operator	Description
# =	Assign a value
# +=	Add and assign
# -=	Subtract and assign
# *=	Multiply and assign
# /=	Divide and assign
# //=	Floor divide and assign
# %=	Modulus and assign
# **=	Exponentiate and assign
# &=	Bitwise AND and assign
# `	=`
# ^=	Bitwise XOR and assign
# >>=	Bitwise right shift and assign
# <<=	Bitwise left shift and assign
# Here's an example that demonstrates how to use assignment operators in Python:
x = 5   # Assigns the value 5 to x
x += 2  # Adds 2 to x and assigns the result to x (equivalent to x = x + 2)
x -= 3  # Subtracts 3 from x and assigns the result to x (equivalent to x = x - 3)
x *= 4  # Multiplies x by 4 and assigns the result to x (equivalent to x = x * 4)
x /= 2  # Divides x by 2 and assigns the result to x (equivalent to x = x / 2)

# Bitwise Operators
# Bitwise operators are used to perform bitwise operations on integer values. Here are the most commonly used bitwise operators in Python:

# Operator	Description
# &	Bitwise AND
# `	`
# ^	Bitwise XOR
# ~	Bitwise NOT
# <<	Bitwise left shift
# >>	Bitwise right shift
# Here's an example that demonstrates how to use bitwise operators in Python:
x = 0b1010   # Binary representation of the decimal number 10
y = 0b0011   # Binary representation of the decimal number 3

# Bitwise AND
print(bin(x & y))  # Output: 0b0010 (binary representation of the decimal number 2)

# Bitwise OR
print(bin(x | y))  # Output: 0b1011 (binary representation of the decimal number 11)

# Bitwise XOR
print(bin(x ^ y))  # Output: 0b1001 (binary representation of the decimal number 9)

# Bitwise NOT
print(bin(~x))     # Output: -0b1011 (binary representation of the decimal number -11)

# Bitwise left shift
print(bin(x << 2)) # Output: 0b101000 (binary representation of the decimal number 40)

# Bitwise right shift
print(bin(x >> 2)) #


# In conclusion, operators are an essential part of Python programming. They allow you to perform mathematical and
# logical operations, assign values to variables, compare values, and perform bitwise operations. By understanding and
# mastering operators, you can write more efficient and effective Python code. Be sure to refer to this lesson and other
# resources as you continue to learn and explore the world of Python programming.