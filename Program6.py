#Write a script to sort (ascending or descending) a dictionary by value

sdict = {
    'Eusebio': 120,
    'Cruyff': 104,
    'Pele': 150,
    'Ronaldo': 132,
    'Messi': 125
    }

sorted_dict = sorted(sdict.items(), key=lambda x:x[1])
print(dict(sorted_dict))