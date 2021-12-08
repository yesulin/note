class Car:
    def drive(self):
        self.wheels = 4  # 实例属性。只出现在方法内部的
        # 只能通过对象访问


car = Car()
car.drive()

print(car.wheels)
# print(Car.wheels)

car.wheels=3  # 可以通过对象进行修改
print(car.wheels)

# 动态添加实例属性
car.color='红色'
print(car.color)