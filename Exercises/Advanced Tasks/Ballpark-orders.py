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
menu = {"Nachos": 6, "Pizza": 6, "Cheeseburger": 10, "Coke": 5, "Water": 4}
tax = 7/100
total = 0
menu_keys = list(menu.keys())
menu_vals = list(menu.values())
order_cost = []

prompt = """
Make an order:

Available meals are: [Nachos], [Pizza], [Cheeseburger], [Coke], [Water]
Separate orders with a space each :::  """

orders = input(prompt).split()
for order in orders:
    if order in menu:
        order_cost.append(menu[order])
    else:
        order_cost.append(menu["Water"])

for i in order_cost:
    total += int(i)

print("\nYour Orders are: {}".format(", ".join(orders)))
print("The prices are: {}".format(str(order_cost)))
print(f"The total for the items is: $ {total} and you have earned 7% discount.")
print("Your pay now is : $ {:.2f}".format(total - (total * tax)))

