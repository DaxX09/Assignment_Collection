"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
   If the given string already ends with 'ing' then add 'ly' instead if the string length of the 
   given string is less than 3,leave it unchanged.

"""

name=input("Enter your name : ")

if len(name)>3:
   name+="ing"
elif name.endswith("ing"):
   name+="ly"
else:
   len(name)<3
   print("Length of the entered name must be more than or eqaul to 3")


print("Modified name:", name)
