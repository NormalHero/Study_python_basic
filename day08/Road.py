#Road.py
class Car:
    def __init__(self,brand="브랜드X",color="색깔X",price=0):
        self.brand = brand
        self.color = color
        self.price = price

    def engineStart(self):
        print(self.brand + " 열쇠로 시동 켜기")

    def engineStop(self):
        print(self.brand+" 열쇠로 시동 끄기")

class SuperCar(Car):
    def __init__(self,brand,color,price,pw):
        #super() : 부모클래스
        super().__init__(brand,color,price)
        self.pw = pw

    def engineStart(self):
        print(self.brand + " 핸드폰으로 시동 켜기")

    def engineStop(self):
        print(self.brand + " 핸드폰으로 시동 끄기")
    
    def roofOpen(self):
        print(self.brand+" 뚜껑 열기")

    def roofClose(self):
        print(self.brand+" 뚜껑 닫기")

mycar = SuperCar("Ferrari","Red",65000,"abcd")
mycar.engineStart()
momcar = Car("K7","White",7000)
momcar.engineStart()
dadcar = Car(price=28000)
#print(dadcar.brand)
#오류 발생
#momcar.roofOpen()

















