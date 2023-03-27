# Lesson: Sets
# In Python, a set is an unordered collection of unique elements. The elements in a set can be of any data
# type such as numbers, strings, and even other sets. In this lesson, we'll cover the basics of creating and working with sets in Python.

# Creating a Set
# To create a set in Python, we use curly braces {} or the set() function. Here's an example:
# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}

# Creating a set using the set() function
my_set = set([1, 2, 3, 4, 5])

# Note that when creating a set using the set() function, we pass in a list of elements.

# Adding and Removing Elements
# To add an element to a set, we use the add() method. To remove an element from a set, we use the remove() method.
# Here's an example:
my_set = {1, 2, 3}

# Adding an element to the set
my_set.add(4)

# Removing an element from the set
my_set.remove(2)

# Set Operations
# Sets support various operations such as union, intersection, difference, and symmetric difference. Here are examples
# of how to perform these operations:
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union of two sets
union_set = set1.union(set2) # Output: {1, 2, 3, 4}

# Intersection of two sets
intersection_set = set1.intersection(set2) # Output: {2, 3}

# Difference of two sets
difference_set = set1.difference(set2) # Output: {1}

# Symmetric difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2) # Output: {1, 4}

# Conclusion
# In conclusion, sets are a useful data structure in Python for storing a collection of unique elements.
# We can create sets using curly braces or the set() function, add or remove elements using the add() and
# remove() methods, and perform various set operations.