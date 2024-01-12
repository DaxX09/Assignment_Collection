"""Write a Python program to get the Fibonacci series of given range."""

a=0
b=1

for i in range (2,6):
    t = a + b
    print (t)
    a=b
    b=t