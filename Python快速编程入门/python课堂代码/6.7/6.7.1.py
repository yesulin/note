def func(num):
    if num==1:
        return 1
    else:
        return num*func(num-1)
num=int(input('请输入一个整数!'))
result=func(num)
print(f'{num}!={result}')
