first_num = int(input("请输入被除数："))
second_num = int(input("请输入除数："))
try:
    res = first_num/second_num # 可能出错的代码
except ZeroDivisionError as error:
    print('异常原因：',error) # 出错了的处理代码
else:
    print("没有错误，正常输出：",res) #没有出错的处理代码
