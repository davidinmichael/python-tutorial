#!/usr/bin/python3

# Write a program that asks the user to enter a sentence and then counts the number of vowels (a, e, i, o, u) in the sentence.
# Write your program below

user_input = input("Enter a Sentence: ")
counter = 0
for ui in user_input:
    if ui in "aeiou":
        counter += 1
print("The number of vowels (a, e, i, o, u) in the " \
    "sentence:\n\"{}\"\nis = {}".format(user_input, counter))
