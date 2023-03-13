# User Inputs
# In Python, you can take input from the user using the input() function. The input() function prompts the user
# to enter some value, and then returns that value as a string. Here's an example:
name = input("What is your name? ")
print("Hello, " + name + "!")

# In this example, the input() function is used to prompt the user to enter their name. The name is then stored
# in the name variable, and a greeting is printed using that variable.

# It's important to note that the input() function always returns a string. If you want to convert the input
# to a different data type (such as an integer or a float), you can use the appropriate conversion
# function (int(), float(), etc.). For example:
age_str = input("How old are you? ")
age = int(age_str)
# In this example, the user is prompted to enter their age as a string. The int() function is then used to convert
# that string to an integer, which is stored in the age variable.
# A shorter way of doing this could be;
age = int(input("How old are you? "))
print(age)
# In this example, the user is prompted for input, and the input is converted to an int


# Printing to the screen
# In Python, you can use the print() function to display output on the screen. The print() function
# takes one or more arguments, which can be strings, variables, or expressions.

# Here are some examples:
print("Hello, World!")   # Output: Hello, World!
# The above example prints the string "Hello, World!" to the screen. The string is enclosed in quotes to
# indicate that it is a string literal.
message = "Hello, Python!"
print(message)   # Output: Hello, Python!
# In this example, we store the message "Hello, Python!" in a variable called message, and then print the
# variable using the print() function.
x = 5
y = 10
print("The sum of", x, "and", y, "is", x+y)   # Output: The sum of 5 and 10 is 15
# In this example, we use the print() function to print a message that includes variables and an expression.
# The variables x and y store the values 5 and 10, respectively. The expression x+y calculates
# the sum of the variables, which is 15.
print("This is the first line.\nThis is the second line.")   # Output: 
                                                             # This is the first line.
                                                             # This is the second line.
# In this example, we use the special character \n to create a new line in the output.
# When the print() function encounters the \n character, it starts a new line in the output.
name = "David"
age = 12
print("My name is {0} and I am {1} years old.".format(name, age))
# This code will output the following:
# My name is David and I am 12 years old.
# In this example, we use the format() method to insert the values of the variables name and age into the string.
# The {0} and {1} are placeholders that are replaced with the values of the first and second arguments passed to
# the format() method, respectively.

# Here is an example using formatted string literals:
name = "Michael"
age = 30
print(f"My name is {name} and I am {age} years old.")
# This code will output the following:
# My name is Michael and I am 30 years old.
# In this example, we use an f-string (formatted string literal) to insert the values of the variables name
# and age into the string. The variables are enclosed in curly braces {} preceded by an f character.
# Both the format() method and f-strings allow you to format and insert variables into a string.


# Comments
# Comments are used to explain what your code does, and to make it more readable for other programmers
# (and for yourself!). In Python, comments start with the # symbol, and continue until the end of the line.
# Every text in this document are comments as they begin with the "#" symbol. When we run our code, comments are usually ignored.