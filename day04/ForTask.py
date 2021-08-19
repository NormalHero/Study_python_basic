#ForTask.py

#for문 문법은 횟수만 지정해서 연습
#언랭
#20,10,0,-10,-20 출력하기
for i in range(20,-30,-10):
    print(i)
    
#1,3,5,7,9,11,13,15,17,... 31 출력하기
for i in range(1,33,2):
    print(i)
    
#n 하나 입력받아서 1 ~ n 까지 출력하기
n = int(input("n : "))
for i in range(1,n+1):
    print(i)

#실버
#1~10까지의 합 출력하기
tot = 0
'''
tot+=1 #1 0+1
tot+=2 #3 0+1+2
tot+=3
tot+=4
tot+=5
tot+=6
tot+=7
tot+=8
'''
for i in range(1,11):
    tot += i
print(tot)

#n,m 입력받아서 n ~ m까지 출력하기
n = int(input("n : "))
m = int(input("m : "))
for i in range(n,m+1):
    print(i)
    
#1~100까지 중 짝수만 출력하기
for i in range(1,101):
    if i%2 == 0:
        print(i)

#골드
#1~100 까지중 3, 5의 공배수 출력하기
#10,30,47,14,1,9,17,174,6,1 출력하기

#플레티넘
#아스키코드 : 각 문자는 대응되는 숫자값을 가지고 있다.
#'A' : 65 / 'B' : 66
#'a' : 97 / 'c' : 99
#'0' : 48
#chr(정수) :  해당하는 아스키코드값을 가진 문자로 변환
#ord('문자') : 해당하는 아스키코드값으로 변환
#A~F 출력하기
#AbCdEf....z 출력하기
#ABCDefghIJKLmnopQRSTuvwxYZ

















