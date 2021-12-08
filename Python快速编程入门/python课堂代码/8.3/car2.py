class Car:
    wheels = 4
    def drive(self):  # 实例方法
        print('我是实例方法,公有的')
car=Car()
print(car.wheels)

# Car.drive() # 实例方法不能通过类名访问
