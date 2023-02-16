#Write a program to split a list every nth element

A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
nth = 4
print ([A[i::nth] for i in range(nth)])