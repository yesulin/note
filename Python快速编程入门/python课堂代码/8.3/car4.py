class Car:
    wheels=4
    @staticmethod
    def test():  # 静态方法,在内部可以通过类名访问类属性
        print('我是静态方法')
        print(f'类属性的值{Car.wheels}')

car=Car()
car.test()
Car.test()