num1=int(input("请输入被除数："))
num2=int(input("请输入除数："))
try:
    print("结果为：",num1/num2) # 可能出错的代码
except ZeroDivisionError as error: # 单个异常
    #except (ZeroDivisionError,ValueError) as error: 多个异常
    #except Exception as error: 全部异常
    print("出错了",error)  # 当出错后，要怎么处理的代码

'''
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ZeroDivisionError: division by zero
'''