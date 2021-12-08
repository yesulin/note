# 定义一个表示人的类
class Person(object): # 父类
    def say_hello(self):
        print("打招呼方式")
# 定义一个表示中国人的类
class Chinese(Person): # 子类
    def say_hello(self):  					# 重写的方法
        super().say_hello() # 引用 父类的say_hello方法
        print("中国人：吃了吗？")
class Bri(Person):
    def say_hello(self):
        super().say_hello()
        print('英国人：hello')
chinese = Chinese()
chinese.say_hello()
bri=Bri()
bri.say_hello()