class Car:
    def __init__(self,color): #构造方法
        # 当使用有参构造方法创建对象时，对象的属性可以有不同的初始值。
        self.color=color
    def drive(self): #实例方法
        print(f'车的颜色为:{self.color}')
car_one=Car('红色')
car_one.drive()
car_one=Car('黄色')
car_one.drive()