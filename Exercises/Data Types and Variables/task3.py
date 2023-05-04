#!/usr/bin/python3

# Write a Python program that converts Fahrenheit temperatures to Celsius temperatures.
# The program should ask the user to enter a temperature in Fahrenheit,and then print the
# equivalent temperature in Celsius.The conversion formula is: C = (F - 32) * 5/9
# write your program below

fah_val = float(input("Temperature (Fahrenheit value): "))

cel_val = (fah_val - 32) * 5/9

print(f"The Celcius equivalent of {fah_val}°F is {cel_val:.2f}°C")

