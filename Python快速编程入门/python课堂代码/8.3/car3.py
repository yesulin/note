class Car:  #类方法
    wheels=4
    @classmethod  # 装饰器，告诉计算机我是类方法
    def stop(cls): # 形参 cls。类方法中可以使用cls访问和修改类的属性的值
        print(cls.wheels)  # cls.whells 是类属性
        cls.wheels=3  # 修改类属性
        print(cls.wheels)

car=Car()
car.stop()
