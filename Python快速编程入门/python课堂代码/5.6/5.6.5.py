old_dict = {'name': 'Jack','age':23,'height':185}
new_dict = {value:key  for key,value in old_dict.items()}
print(new_dict)
