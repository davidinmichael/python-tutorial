# Classes and objects are fundamental concepts in object-oriented programming(OOP).
# They allow you to create reusable
# and structured code by defining blueprints for objects.

# Classes
# A class is a blueprint for creating objects. It defines the properties (attributes)
# and behaviors (methods) that objects of that class will have. Classes are defined
# using the class keyword.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")


# In the above example, we define a Dog class with attributes name and age,
# and a method bark that prints a bark message.

# Objects
# An object is an instance of a class. It represents a specific entity based on the
# blueprint provided by the class. Objects are created using the
# class constructor method __init__.

my_dog = Dog("Buddy", 3)
your_dog = Dog("Molly", 5)

my_dog.bark()  # Output: Buddy says Woof!
your_dog.bark()  # Output: Molly says Woof!
