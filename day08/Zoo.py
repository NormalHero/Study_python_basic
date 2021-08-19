#Zoo.py
#동물 세마리 울게 만들기(울음소리 다르게)
#이름, 성별, 나이
#울기, 움직이기
class Animal:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def makeSomeNoise(self):
        print("울기")

    def move(self):
        print("움직이기")

#별코두더지  
class Condylura(Animal):
    def makeSomeNoise(self):
        print("두더더어더ㄷ커덕")

    def move(self):
        print("땅에서 보이지 않게 움직인다.")

class Unicorn(Animal):
    def makeSomeNoise(self):
        print("히이이이힝")

    def move(self):
        print("뿔을 세워서 들이받는다.")

#왈라비
class Wallaby(Animal):
    def makeSomeNoise(self):
        print("아웃백가자")

    def move(self):
        print("훅훅 스트레이트")

c = Condylura("김두더지","수컷",5)
u = Unicorn("이유니콘","암컷",7)
w = Wallaby("박왈라비","수컷",10)

while True:
    c.makeSomeNoise()
    u.makeSomeNoise()
    w.makeSomeNoise()





    
    
