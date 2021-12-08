class Car:
    def __init__(self): #构造方法 无参数
        # 使用无参构造方法创建对象时，所有对象的属性都有相同的初始值。
        self.color='红色'
        print('创建对象时，自动实现初始化')

    def drive(self): #实例方法
        print(f'车的颜色为:{self.color}')

car_one=Car()
car_one.drive()

car_two=Car()
car_two.drive()