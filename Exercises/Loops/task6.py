#!/usr/bin/python3
import random

# Write a program that generates a random number between 1 and 100 and asks the user to guess the number.
# The program should keep asking the user to guess until they get the number right, and then print out the number of guesses it took.
# Write your program below

gen = random.randint(1, 101)
count = 0


while True:
    guess = int(input("Guess a number from 1 - 10: "))
    count = count + 1
    if guess == gen:
        print("Correct! You guessed right.")
        break
    else:
        print("Ooops! Try again.")
print(f"You tried {count} times")