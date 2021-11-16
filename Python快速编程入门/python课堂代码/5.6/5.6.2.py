# 第一种方法
d2={'ye':'叶','B':456}
print(d2['ye'],d2['B'])

# 第二种方法 内置的get()
print(d2.get('ye'))

# 第三种方法 keys(),valus(),items()
dic={'name':'jack','age':23,'height':185}
print(dic.keys()) #打印所有的 键
print(dic.values()) # 打印所有 值
print(dic.items())

for key in dic.keys(): # 经常会用到的方式
    print(key)

# 思考：能不能用遍历的方法打印出所有的值或键值？？