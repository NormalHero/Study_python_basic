#ExceptionTest.py
'''
try:
    print(int("10"))
    print(int("Hello"))
    print(int("32"))
except ValueError:
    print("정수로 바꿀 수가 없어요~")
'''

try:
    num1 = int(input("정수1 : "))
    num2 = int(input("정수2 : "))
    print("결과 :",num1//num2)
except ValueError:
    print("정수만 입력하세요.")
except ZeroDivisionError:
    print("0으로는 나눌 수 없어요.")
except Exception as e:
    print("알 수 없는 오류 발생 / 개발자에게 알려주세요.")
    #print(type(e))














