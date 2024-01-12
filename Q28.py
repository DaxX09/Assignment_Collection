# Write a Python function to insert a string in the middle of a string.
s1=input("Enter string:-")
s2=input("Enter 2nd string:-")


s3=s1[:2]+s2+s1[-2:]

print(s3)
