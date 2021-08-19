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
def div(num1,num2):
    return num1/num2
#n부터 m까지의 합 구해주는 함수
def sumNTOM(n,m):
    tot = 0
    for i in range(n,m+1):
        tot += i
    return tot
#어떤 문자열을 n번만큼 출력하는 함수
def printMsg(msg,n):
    for i in range(n):
        print(msg)

#""+"a" --> "a" + "b" --> "ab"
#a : 97  b : 98
#A : 65  B : 66
#소문자를 대문자로 바꿔주는 함수("hEl~Lo!!123" -> "HEL~LO!!123")
def changeToUpperCase(msg):
    result = ""
    for ch in msg:
        if ch>='a' and ch<='z':
            result += chr(ord(ch)-32)
        else:
            result += ch
        #result += chr(ord(ch)-32) if ch>='a' and ch<='z' else ch
    return result
#01234
#HELLO
#문자열을 거꾸로 출력하는 함수("HELLO" -> "OLLEH")
def reverse(msg):
    result = ""
    '''
    for ch in msg:
        result = ch + result
    '''
    for i in range(len(msg)-1,-1,-1):
        result += msg[i]
    print(result)
    
#정수를 한글로 바꿔주는 함수(1024 -> "일공이사")
def changeToHangle(num):
    hangle = "공일이삼사오육칠팔구"
    data = str(num)                 #1024 -> "1024"
    result = ""
    for ch in data:
        idx = int(ch)               #"1" "0" "2" "4" -> 1 0 2 4
        result += hangle[idx]       #"일" "공" "이" "사"
    return result

##############################
print1To10()
print(sum1To10())
print(sum1ToN(100))

print(changeToUpperCase("hEl~Lo!!123"))
print("hEl~Lo!!123".upper())
print(changeToHangle(102313546876511))
























