#Write a program to extract numbers from a given string.

str = 'red 12 black 45 green'
result = [int(str) for str in str.split() if str.isdigit()]
print(result)