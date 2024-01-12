"""Write a Python program to check if a number is positive, negative or zero."""

positive_count=0
negative_count=0
for i in range(1,6):
    num=int(input("Enter a number:-"))
    if num>0:
     positive_count+=0
    else:
     negative_count+=0
print("Positive Number",positive_count)
print("Negative Number",negative_count)
