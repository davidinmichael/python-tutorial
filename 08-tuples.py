# tuple
# In Python, a tuple is an immutable sequence of values, separated by commas and enclosed in parentheses ().
# Once a tuple is created, its values cannot be changed. Tuples are useful for representing fixed collections
#     of related values, such as the coordinates of a point or the RGB values of a color.

# To create a tuple in Python, simply separate the values with commas and enclose them in parentheses:
my_tuple = (1, 2, 3)
# You can also create a tuple using the built-in tuple() function:
my_tuple = tuple([1, 2, 3])
# Tuples are similar to lists in many ways, but with a few key differences:

# Tuples are immutable, meaning you can't add or remove elements after the tuple is created.
# Tuples are typically used to group related values together, while lists are used for more general-purpose collections of values.
# Tuples can be used as dictionary keys, while lists cannot.
# You can access individual elements of a tuple using indexing:
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
# You can also use slicing to access a range of elements in a tuple:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)
# Since tuples are immutable, you cannot modify their values directly. However, you can create a new tuple with modified
# values using concatenation or slicing:
my_tuple = (1, 2, 3)
new_tuple = my_tuple[:2] + (4,)  # create a new tuple with the first two elements of `my_tuple` and a new value of 4
print(new_tuple)  # Output: (1, 2, 4)
# In addition to indexing and slicing, you can also use the len() function to get the length of a tuple:
my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3
# And you can use the in keyword to check if a value is in a tuple:
my_tuple = (1, 2, 3)
print(2 in my_tuple)  # Output: True

# Conclusion:
# Tuples are useful for representing fixed collections of related values that don't need to be modified.
# They are similar to lists, but with a few key differences such as immutability and being used more often
# to group related values together. Tuples can be created using parentheses or the tuple() function, and
# accessed using indexing, slicing, and the len() function.