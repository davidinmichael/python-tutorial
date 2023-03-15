# Loops are a fundamental concept in programming, allowing you to repeat a section of code multiple times.
# In Python, there are two main types of loops: for loops and while loops.

# For Loops
# A for loop is used when you want to execute a block of code a fixed number of times, or when you want to iterate
# over a collection of elements (like a list, tuple, or string). The basic syntax of a for loop is as follows:
# for variable in sequence:
    # code to be executed for each element

# Here, variable is a temporary variable that takes on the value of each element in sequence in turn.
# The code inside the loop (indented under the for statement) is executed once for each element in sequence.

# Here's an example of a simple for loop that prints the numbers 1 to 5:
for i in range(1, 6):
    print(i)
# In this example, range(1, 6) generates a sequence of numbers from 1 to 5, which are then printed to the
# console by the print function.

# While Loops
# A while loop is used when you want to execute a block of code repeatedly until a certain condition is met.
# The basic syntax of a while loop is as follows:
# while condition:
    # code to be executed while condition is true
# Here, condition is an expression that is evaluated at the beginning of each iteration of the loop.
# If condition is true, the code inside the loop is executed; if condition is false, the loop is exited and
# execution continues with the next statement after the loop.

# Here's an example of a simple while loop that prints the numbers 1 to 5:
i = 1
while i <= 5:
    print(i)
    i += 1
# In this example, i starts at 1 and is incremented by 1 on each iteration of the loop. The loop continues as long
# as i is less than or equal to 5, printing the current value of i to the console each time.

# Loop Control Statements
# Python provides a number of loop control statements that allow you to modify the behavior of loops. These include:

# break: Exit the loop immediately.
# continue: Skip the rest of the code inside the loop for the current iteration and move on to the next iteration.
# pass: Do nothing and move on to the next statement.
# These statements can be used in both for and while loops to control the flow of execution.

# That's a brief introduction to loops in Python! With these concepts in mind, you should be able to write simple
# programs that use loops to repeat code and iterate over collections.

# Here are examples on them: Run each of them to see the output
# break:
for i in range(10):
    if i == 5:
        break
    print(i)
# Explanation: The loop starts with i=0 and iterates up to i=4. When i=5, the break statement is executed,
# causing the loop to exit immediately.

# continue:
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Explanation: The loop starts with i=0 and iterates up to i=9. When i is even, the continue statement is executed,
# causing the code inside the loop for that iteration to be skipped, and the loop moves on to the next iteration.

# pass:
for i in range(10):
    if i == 5:
        pass
    print(i)
# Explanation: The loop starts with i=0 and iterates up to i=9. When i=5, the pass statement is executed,
# causing the code to do nothing and move on to the next statement.The loop then continues normally.