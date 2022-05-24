list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
new_list=[]
for item in list1:
    if item in list2:
        new_list.append(item)
print(new_list)


