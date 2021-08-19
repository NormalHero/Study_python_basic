#Import2.py

#random
#random 모듈을 r 이라는 별칭으로 추가
import random as r
import time as t

#.(하위 연산자)
#A.b : A 안의 b, A 의 b

#r.random() : 0~1 사이의 랜덤한 실수 반환
#r.randrange(n,m) : n~m 사이의 랜덤한 정수 반환
'''
while True:
    #print(r.random())
    print(r.randrange(1,11))
'''
'''
#t.time() : 1970년 1월 1일 0시 0분 0초 ~ 현재 흐른 초 반환
now=t.time()
print(now)
print(t.localtime(now))
#ctime() : 현재 시간을 간편하게 표현
print(t.ctime())
'''
#t.sleep(n) : n초만큼 프로그램 진행을 멈추기
'''
print("3초 세기 시작!")
t.sleep(3)
print("3초가 지났습니다.")
'''
'''
while True:
    print(r.randrange(100,1000))
    t.sleep(0.5)
'''

#import webbrowser as w
#w.open("https://www.google.com")















