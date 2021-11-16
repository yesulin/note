# 索引
list=['java','c#','python','PHP']
print(list[0])
print(list[-1])

# 切片
li=['p','y','t','h','o','n']
print(li[0:3])
print(li[0:4:2])
print(li[2:])
print(li[:4])
print(li[:])

for l in li:
    print(l,end=' ')

print()
print('y' in li) # 存在于li中
print('y' not in li) # 不存在于li中