"""
Write a program to convert list to list of dictionaries
"""

list1 = ["Black","Red","Maroon","Yellow"]
list2 = ["#000000","#FF0000","#800000","#FFFF00"]
final_list = []

for i in range(len(list1)):
    final_list.append({"color_name" : list1[i], "color_code": list2[i]})

print(final_list)