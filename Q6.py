"""Write a Python program to get the Factorial number of given number."""

import math

num = int(input("Enter a non-negative number: "))

result = math.factorial(max(0, num))

print(f"The factorial of {num} is {result}")
# 