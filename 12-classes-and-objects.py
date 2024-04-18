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


# In Python, self is a reference to the current instance of a class. It is used within
# methods of a class to access and modify attributes and call other methods on the
# same object. The use of self helps differentiate between class attributes and instance
# attributes, allowing each instance of a class to maintain its own state.

# Objects
# An object is an instance of a class. It represents a specific entity based on the
# blueprint provided by the class. Objects are created using the
# class constructor method __init__.

my_dog = Dog("Buddy", 3)
your_dog = Dog("Molly", 5)

my_dog.bark()  # Output: Buddy says Woof!
your_dog.bark()  # Output: Molly says Woof!


# In the above code, we create two instances of the Dog class, my_dog and your_dog,
# each with its own name and age. We then call the bark method on each object.


# Attributes
# Attributes are variables associated with a class or object. They represent the state
# of the object. You can access and modify attributes using dot notation.

print(my_dog.name)  # Output: Buddy
print(your_dog.age)  # Output: 5

my_dog.age = 4
print(my_dog.age)  # Output: 4


# Methods
# Methods are functions associated with a class or object. They define behaviors
# that objects of the class can perform. Methods can access and modify object attributes.

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * self.radius ** 2

my_circle = Circle(5)
area = my_circle.calculate_area()
print(area)  # Output: 78.53975


# In this example, we define a Circle class with an attribute radius and a method
# calculate_area that computes the area of the circle.

# Constructor Method
# The constructor method __init__ is a special method used to initialize objects of a class.
# It is called automatically when an object is created.

# Conclusion
# Classes and objects are essential concepts in object-oriented programming.
# They help organize code into reusable components and represent real-world entities.
# Classes define attributes and methods, while objects are instances of classes with
# specific attribute values. Understanding classes and objects is crucial for building
# complex and structured programs in Python.
