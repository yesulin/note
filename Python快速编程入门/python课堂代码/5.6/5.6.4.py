dic={'name':'jack','age':23,'height':185}
print(dic.pop('height')) # 删除指定的键对应的值
print(dic)

dic1={'name':'jack','age':23,'height':185}
print(dic1.popitem()) #随机删除
print(dic1)

dic2={'name':'jack','age':23,'height':185}
dic2.clear() # 清空
print(dic2)