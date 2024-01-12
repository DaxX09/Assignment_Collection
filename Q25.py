"""Write a Python function that takes a list of words and returns the length of the longest one.a"""

l1=["Python","Java","Android","Hello"]

max=len(l1[0])

word=""

for i in l1:
    if len(i)>max:
        word=i
        max=len(i)
    
print("max=",max)
print("word=",word)
