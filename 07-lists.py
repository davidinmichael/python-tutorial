# Lists
# Lists are a fundamental data structure in Python. A list is an ordered collection of elements that can be of any data type.
# Lists are mutable, which means you can modify their contents.

# Creating a List
# To create a list, simply enclose a comma-separated sequence of values in square brackets [].
my_list = [1, 2, 3, 'four', 5.0]
# You can also create an empty list using empty square brackets.
empty_list = []

# Accessing Elements
# You can access individual elements of a list using indexing. The first element in a list has an index of 0.
my_list = [1, 2, 3, 'four', 5.0]
print(my_list[0]) # 1
print(my_list[3]) # 'four'

# You can also use negative indexing to access elements from the end of the list.
my_list = [1, 2, 3, 'four', 5.0]
print(my_list[-1]) # 5.0
print(my_list[-3]) # 3

# Slicing Lists
# You can extract a sublist from a list using slicing. Slicing is done using the colon : operator.
my_list = [1, 2, 3, 'four', 5.0]
print(my_list[1:3]) # [2, 3]
print(my_list[:2]) # [1, 2]
print(my_list[3:]) # ['four', 5.0]

# Modifying Lists
# Lists are mutable, which means you can modify their contents.
# You can modify a specific element by assigning a new value to its index.
my_list = [1, 2, 3, 'four', 5.0]
my_list[2] = 'three'
print(my_list) # [1, 2, 'three', 'four', 5.0]

# You can also add elements to the end of a list using the append() method.
my_list = [1, 2, 3, 'four', 5.0]
my_list.append(6)
print(my_list) # [1, 2, 3, 'four', 5.0, 6]

# You can remove an element from a list using the remove() method.
my_list = [1, 2, 3, 4]
my_list.remove(2) # The removes the number 2 from the list

# Here are some common list methods:

# append(item): adds an item to the end of the list
# extend(list): adds the elements of another list to the end of the list
# insert(index, item): inserts an item at a specific index in the list
# remove(item): removes the first occurrence of an item from the list
# pop(index): removes and returns the item at a specific index in the list
# index(item): returns the index of the first occurrence of an item in the list
# count(item): returns the number of times an item appears in the list
# sort(): sorts the items in the list in ascending order
# reverse(): reverses the order of the items in the list

# In conclusion, lists are a fundamental data structure in Python that can be used to store and manipulate
# collections of items. They are mutable, versatile, and can be accessed by index, allowing for efficient manipulation of data.