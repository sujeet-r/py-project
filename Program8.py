#Write a program to remove duplicate words from a given string.
#Check Commit

str = 'Python Exercises Practice Solutions Exercises'

split_list = str.split()
temp = []
for i in split_list:
    if i not in temp:
        temp.append(i)
print(' '.join(temp))
