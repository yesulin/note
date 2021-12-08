class Car:
    def __init__(self): # 构造方法 无参
        self.color = "蓝色"
        print("对象被创建")
    def __del__(self): # 当删除对象后，自动调用析构方法
        print("对象被销毁")
car = Car()
print(car.color)
del car # 删除对象
print(car.color)
