class ShortInputError(Exception):  #自定义异常类n 继承Exception类或Exception子类的类 （类名一般以“Error”为结尾)
    '''自定义异常类'''
    def __init__(self, length, atleast):
        self.length = length  	            # 输入的密码长度
        self.atleast = atleast  	            # 限制的密码长度
try:
    text = input("请输入密码：")
    if len(text) < 3:
        raise ShortInputError(len(text), 3)
except ShortInputError as result: # result相当于对象名
    print("ShortInputError：输入的长度是%d，长度至少应是 % d" %
          (result.length, result.atleast)) # 访问实例属性
else:
    print("密码设置成功")
