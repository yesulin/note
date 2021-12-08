'''
让不同类的同一功能可以通过同一个接口调用，表现出不同的行为。
'''
class Car:
    def shout(self):
        print('喵。。。。。')

class Dog:
    def shout(self):
        print('汪。。。。。')

def shout(obj):
    obj.shout()

car=Car()
dog=Dog()
shout(car)
shout(dog)