#Quiz.py
'''
print("다음 중 프로그래밍 언어가 아닌것은?\
               \n1. 파이썬\n2. C언어\n3. 망둥어\n4. Java")
choice = input()
'''
choice = input("다음 중 프로그래밍 언어가 아닌것은?\
               \n1. 파이썬\n2. C언어\n3. 망둥어\n4. Java\n")
'''
#분기처리
if choice == '3':
    print("정답입니다.")
elif choice == '1' or choice == '2' or choice == '4':
    print("오답입니다.")
else:
    print("잘못 입력하셨습니다.")
'''
#일괄처리
result = ""
if choice == '3':
    result = "정답입니다."
elif choice == '1' or choice == '2' or choice == '4':
    result = "오답입니다."
else:
    result = "잘못 입력하셨습니다."
print(result)

#if 1<=num and num<=100:
#if 1<=num<=100:

#if id=="apple" and pw=="1234":
    #print("로그인 성공")













