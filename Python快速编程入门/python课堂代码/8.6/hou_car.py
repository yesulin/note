class House(object): # 父类 房子类
    def live(self):
        print("居住")
class Car(object): # 父类 汽车类
    def drive(self):
        print("行驶")

class Tcar(House,Car): # 子类 房车类
    pass

tcar=Tcar()
tcar.live()
tcar.drive()