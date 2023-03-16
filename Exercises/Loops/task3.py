#!/usr/bin/python3

# Write a program that asks the user to input a series of numbers and then calculates the average of those numbers.
# Write your program below

if __name__ == "__main__":
    import sys as s

    total = 0 # the sum of all values
    arg_count = len(s.argv) - 1 # number of arguments passed
    if arg_count == 0:
        print("Enter series of numbers separated with comma")
        n_temp = list(input().split())
        for n in n_temp:
            total += int(n)
        print("The sum of {} = {}".format(n_temp, total))
        exit(0)
    else:
        nums = []
        for num in range(arg_count):
            total += num
            nums.append(num)
        print("The sum of {} = {}".format(nums, total))
