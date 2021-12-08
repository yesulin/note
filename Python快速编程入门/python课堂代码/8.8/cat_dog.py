'''
多态是面向对象的重要特性之一，它的直接表现即让不同类的同一功能可以通过同一个接口调用，表现出不同的行为。
'''


class Cat:
    def shout(self):  # 实例方法
        print("喵喵....")


class Dog:
    def shout(self):
        print("汪汪....")


def shout(obj):  # 同一个接口 函数定义
    obj.shout()


cat = Cat()  # 创建对象
dog = Dog()

shout(cat)  # 函数调用
shout(dog)
