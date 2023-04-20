#!/usr/bin/python3

# Write a program that asks the user to input a series of numbers and then calculates the average of those numbers.
# Write your progam below

num = int(input("How many numbers do you want to enter: "))
sum_of_nums = 0
count = 1
num_list = []

for nos in range (num):
    nums = float(input(f"Enter number {count}: "))
    sum_of_nums += nums 
    count += 1
    num_list.append(nums)
    
average = sum_of_nums / num
print(f"The average of numbers: {num_list} = {average}")

