#Road.py
class Car:
    brand=""
    color=""
    price=0

    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price

    def engineStart(self):
        print(self.brand+" 시동 켜기")

    def engineStop(self):
        print("시동 끄기")

    def info(self):
        print("주소값 :",self)
'''
mycar = Car()
mycar.brand = "Ferrari"
momcar = Car()
momcar.brand = "K7"
mycar.engineStart()
momcar.engineStart()

#mycar.info()
#print(mycar)
'''
mycar = Car("Ferrari","Red",65000)
momcar = Car("K7","White",7000)





















