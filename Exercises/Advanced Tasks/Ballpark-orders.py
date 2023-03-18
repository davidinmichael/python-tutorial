#!/usr/bin/python3

# You and three friends go to a baseball game. You offer to go to the concession stand for everyone.
# They each order one thing, and you do as well. Nachos and Pizza both cost $6.00. A Cheeseburger meal costs $10.
# Water is $4.00 and Coke is $5.00. Tax is 7%.

# Task 
# Determine the total cost of ordering four items from the concession stand. If one of your friend’s orders
# something that isn't on the menu, you will order a Coke for them instead.

# Input Format
# You are given a string of the four items that you've been asked to order that are separated by spaces.

# Output Format 
# You will output a number of the total cost of the food and drinks.

# Sample Input 
# 'Pizza Cheeseburger Water Popcorn'

# Sample Output 
# 26.75
menu = {"Nachos": 6, "Pizza": 6, "Cheeseburger": 10, "Water": 4, "Coke": 5}
tax = 7/100
total = 0
