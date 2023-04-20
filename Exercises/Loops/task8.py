#!/usr/bin/python3

# Write a program that asks the user to enter a sentence and then counts the number of vowels (a, e, i, o, u) in the sentence.
# Write your program below

sentence = input("Enter a sentence: ").lower()
count = 0

for vowel in sentence:
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
        count = count + 1
print(f"The total number of vowels in your sentence is {count}")