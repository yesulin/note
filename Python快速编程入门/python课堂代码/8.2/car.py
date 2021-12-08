class Car:  # 类名，首字母大写，符合标识符
    wheels=4  # 属性（放在类外它就是变量）
    def drive(self):  # 方法，小括号中第一个参数self.（其它放到类外它就是函数）
        print("行驶")  # 方法体

car=Car()
# 对象名=类名()
# 有了对象后就可以使用类的属性或方法
print(f"汽车有{car.wheels}只轮胎")
car.drive()

