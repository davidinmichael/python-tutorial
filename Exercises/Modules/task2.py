#!/usr/bin/python3
import random 

# Write a program that imports the random module and uses the randrange function to 
# generate a random integer
# between 1 and 100 (inclusive). Then, ask the user to guess the number andgive them 
# feedback on whether their
# guess was too high, too low, or correct.

# Write your program below

rand_range = random.randrange(1, 101)
count = 0

while True:
    guess = int(input("Guess a number from 1 - 100: "))
    count = count + 1
    if guess == rand_range:
        print("Correct! You guessed right.")
        break
    elif guess < rand_range:
        print("Too low. Try again.")
    elif guess > rand_range:
        print("Too high. Try again.")
print(f"You tried {count} times")