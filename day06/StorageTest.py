#StorageTest.py
x = 10000000000
def f1():
    print(x)
def f2():
    data = 100
#f1()
'''
#지역변수는 외부에서 사용 불가하다.
print(data)
'''
#f3() 내부에는 x라는 변수가 없으므로 대입연산자를 이용해서 값을 넣는 순간
#x라는 변수가 지역변수로 선언된다. 전역변수는 함수 내에서 수정할 수 없다.
'''
def f3():
    x=10000

f3()
print(x)
'''

arData = [10,20,30]
#arData는 세개의 값이 존재하는 공간의 주소값을 가지고 있다.
#arData.append 라는 뜻은 arData가 가지고 있는 주소로 이동해서
#그 곳에 새로운 값을 추가해라! 라는 뜻이기 때문에
#실제 arData라는 주소값을 가지고 있는 공간은 수정이 되지 않았고
#그렇기 때문에 함수 내부에서 .append()는 사용이 가능하다.
def f4():
    arData.append(40)
'''

f4()
print(arData)
'''
def f5():
    global x    #전역변수 x
    x=10

f5()
print(x)



















