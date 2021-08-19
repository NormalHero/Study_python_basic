#FunctionTest.py
#f(x) = 2x + 1
def f(x):
    #while True:
    #    print("함수!!!!!!")
    return 2*x+1

#내 이름("정다솔") 열번 출력하는 함수
def printName():
    for i in range(10):
        print("정다솔")

#넘겨주는 수에 맞는 단(구구단의 단) 출력하는 함수
def printDan(dan):
    for i in range(1,10):
        print(dan,"X",i,"=",dan*i)




print(f(3))
#data=input()
#print()
#f()
printName()
n = input()
printDan(n)























