#FunctionTask.py

#1~10까지 출력하는 함수
def print1To10():
    for i in range(1,11):
        print(i)
#1~10까지의 합 구해주는 함수
def sum1To10():
    tot = 0
    for i in range(1,11):
        tot += i
    return tot

#1~n 까지의 합 구해주는 함수
def sum1ToN(n):
    tot = 0
    for i in range(1,n+1):
        tot += i
    return tot
    
#두 정수의 나눗셈 함수
#n부터 m까지의 합 구해주는 함수
#어떤 문자열을 n번만큼 출력하는 함수


#""+"a" --> "a" + "b" --> "ab"
#소문자를 대문자로 바꿔주는 함수("hEl~Lo!!123" -> "HEL~LO!!123")
#문자열을 거꾸로 출력하는 함수("HELLO" -> "OLLEH")
#정수를 한글로 바꿔주는 함수(1024 -> "일공이사")
##############################
print1To10()
print(sum1To10())
print(sum1ToN(100))


























