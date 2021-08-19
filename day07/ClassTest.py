#ClassTest.py
class Albamon:
    #알바생이 가지고 있을 성질들(속성들)
    #알바생의 이름
    name = ""
    #알바생의 성별
    gender = ""
    #알바생의 나이
    age = 0
    #알바생의 경력           
    ref = 0

    #알바생이 해야할 기능들
    #재료구매 기능
    def buy():
        print("재료사기")
    #진열하기 기능
    def display():
        print("진열하기")
    #판매하기 기능
    def sell():
        print("판매하기")

#객체화
alba1=Albamon()
alba2=Albamon()
alba1.name = "정다솔"
alba1.gender = "남성"
alba1.age = 22
alba1.ref = 10
#abla1_name = "정다솔"
print(alba1.name)
#오류발생
#alba1.buy()
















        
