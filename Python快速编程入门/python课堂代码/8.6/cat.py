class Cat(object): #父类
    def __init__(self,color):
        self.color=color
        # self.__age=1 只能继承公有方法或属性
        self.age=1
    def walk(self):
        print("走猫步。。。")

class Sfold(Cat): # 子类 波斯猫的类，单继承
    pass #略，什么代码都不写

flod=Sfold('灰色') # 拿儿子的类，进行实例化，创建flod对象
print(f'{flod.color}的波斯猫，今年{flod.age}岁')
flod.walk()


