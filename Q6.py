from hashlib import new


string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
new_list=[]
for item in string_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)