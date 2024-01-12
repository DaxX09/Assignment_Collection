"""
Write a Python program that will return true if the two given integer values are equal 
   or their sum or difference is 5
"""
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = (num1 == num2) or (num1 + num2 == 5) or (num1 - num2 == 5) or (num2 - num1 == 5)

if result:
    print("True")
else:
    print("False")
