class Car:
    wheels = 4  # 类属性。类内部，方法外部
                # 可以通过 类或对象，但只有类才能修改
    def drive(self):
        print("行驶")


car = Car()
print(Car.wheels)  # 类访问
print(car.wheels)  # 对象访问

Car.wheels = 3
print(Car.wheels)  # 类访问
print(car.wheels)  # 对象访问

car.wheels = 5  # 动态添加实例属性
print(Car.wheels)  # 类访问
print(car.wheels)  # 对象访问 实例属性
