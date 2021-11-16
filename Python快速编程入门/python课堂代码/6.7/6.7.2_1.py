def p(n): # 普通函数p 带形参
    print(f'平方',n*n)
p(5)

p=lambda n:n*n # 用匿名函数改写
print(f'平方{p(10)}')