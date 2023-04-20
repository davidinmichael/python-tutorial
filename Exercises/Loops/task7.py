#!/usr/bin/python3

# Write a program that asks the user to enter a series of words and then prints out the words in alphabetical order.
# Write your program below

words = input("Enter a series of words: ")
word_list = words.split()
arranged_list = sorted(word_list)

for word in arranged_list:
    print(word.lower())
