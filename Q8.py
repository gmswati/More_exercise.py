list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
list1+=list2
new_list=[]
for item in list1:
    if item not in new_list:
        new_list.append(item)
print(new_list)
