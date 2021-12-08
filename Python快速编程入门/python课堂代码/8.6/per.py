class Person:  # 定义类
    def __init__(self, name):  # 构造方法，初始化
        self.name = name
        self.__age = 1  # 这个私有属性，只有通过公有方法访问或修改

    def set_age(self, new_age):  # 修改私有属性
        if 0 < new_age <= 120:
            self.__age = new_age

    def get_age(self):  # 通过公有方法，获取私有属性
        return self.__age


persor = Person('小明')
persor.set_age(20)
print(f'{persor.name}的年龄为{persor.get_age()}岁')
