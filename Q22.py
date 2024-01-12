"""
Write a Python program to get a single string from two given strings, separated 
   by a space and swap the first two characters of each string
"""

s1="Python"
s2="Java"

new_s1=s1[:1]+s2[1:]
print(new_s1)

new_s2=s2[:1]+s1[1:]
print(new_s2)
