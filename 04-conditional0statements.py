# Conditional statements in Python allow you to execute different blocks of code depending on whether a
# certain condition is true or false. The most common types of conditional statements are
# the if, elif, and else statements.

# Here is an example of an if statement:
x = 5
if x > 0:
    print("x is positive")
# In this example, we use the if statement to check if the value of x is greater than 0.
# If the condition is true, the indented block of code under the if statement is executed,
# which prints the message "x is positive" to the screen.

# Here is an example of an if-else statement:
x = -3
if x > 0:
    print("x is positive")
else:
    print("x is not positive")
# In this example, we use the if-else statement to check if the value of x is greater than 0.
# If the condition is true, the first indented block of code under the if statement is executed,
# which prints the message "x is positive" to the screen. If the condition is false, the second
# indented block of code under the else statement is executed, which prints the message "x is not positive" to the screen.

# Here is an example of an if-elif-else statement:
x = 10

if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")
# In this example, we first check if x is less than 0. If it is, we print "x is negative".
# If x is not less than 0, we move on to the next condition, which checks if x is equal to 0.
# If x is equal to 0, we print "x is zero". If x is not less than 0 and not equal to 0,
# we move on to the final else statement, which prints "x is positive".

# Note that the elif statement is optional. You can have as many or as few elif statements
# as you need, or you can omit them altogether.

# Here's another example:
age = 18

if age < 18:
    print("You are too young to vote.")
elif age >= 18 and age < 21:
    print("You can vote, but you can't drink.")
else:
    print("You can vote and drink.")
# In this example, we check if age is less than 18. If it is, we print "You are too young to vote.".
# If age is not less than 18, we move on to the next condition, which checks if age is between 18 and 21 (inclusive).
# If age is between 18 and 21, we print "You can vote, but you can't drink.". If age is not less than 18 and
# not between 18 and 21, we move on to the final else statement, which prints "You can vote and drink.".

# By using elif, we can check multiple conditions and print different messages depending on the value of
# the variable being checked.