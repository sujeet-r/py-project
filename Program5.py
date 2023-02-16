"""
Write a program to get a string made of the first 2 and the last 2 chars from a given string.
"""

str = 'w3resource'

if(len(str)<2):
    print("Empty String")
else:
    print(str[:2]+str[-2:])