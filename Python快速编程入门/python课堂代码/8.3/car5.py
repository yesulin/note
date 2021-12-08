class Car:
    __wheels=4  # 私有属性
    def __drive(self): # 私有方法
        print("行驶")
    def test(self):    # 公有方法
        print(f'轿车有{self.__wheels}个轮') #通过公有方法内部访问私有成员
        self.__drive()
car=Car()
# print(car.wheels)
# car.drive()
car.test()