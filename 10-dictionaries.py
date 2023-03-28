# In Python, a dictionary is a collection of key-value pairs, where each key is unique and mapped to a
# corresponding value. Dictionaries are also known as associative arrays or hash tables in other programming languages.
# my_dict = {key1: value1, key2: value2, key3: value3}
# Here, keys and values can be of any data type. Keys must be immutable objects, such as strings, numbers, or tuples.
# Values can be of any data type, including lists, tuples, and even other dictionaries.

# Accessing Values in a Dictionary:
# You can access the values in a dictionary using their corresponding keys. You can also use the get() method to retrieve
# the value of a key, which returns None if the key is not found.
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

print(my_dict['name'])  # Output: John
print(my_dict.get('age'))  # Output: 25
print(my_dict.get('salary'))  # Output: None

# Adding and Modifying Key-Value Pairs in a Dictionary:
# You can add new key-value pairs to a dictionary by using the key as the index and assigning it a value.
my_dict = {'name': 'John', 'age': 25}

# Adding a new key-value pair
my_dict['city'] = 'New York'

# Modifying an existing key-value pair
my_dict['age'] = 26

print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'New York'}

# Removing Key-Value Pairs in a Dictionary:
# You can remove a key-value pair from a dictionary using the del keyword or the pop() method.
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Removing a key-value pair using del
del my_dict['city']

# Removing a key-value pair using pop
my_dict.pop('age')

print(my_dict)  # Output: {'name': 'John'}

# Looping Through a Dictionary:
# You can use a for loop to iterate over a dictionary. By default, the loop will iterate over the keys of the dictionary.
# You can also use the items() method to loop over both the keys and values of the dictionary.
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Looping over keys
for key in my_dict:
    print(key)

# Looping over values
for value in my_dict.values():
    print(value)

# Looping over keys and values
for key, value in my_dict.items():
    print(key, value)

# Conclusion:
# Dictionaries are a useful data structure in Python for storing and retrieving key-value pairs. They are flexible and can
# contain values of any data type. You can access, add, modify, and remove key-value pairs using various methods.
# Looping through a dictionary allows you to iterate over its keys and values, making it easy to process the data stored in the dictionary.