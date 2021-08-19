#OperTest.py
num = int(input("정수 : "))

#print("양수입니다.") if num>0 else print("음수입니다.")

result = "양수입니다." if num>0 else ("음수입니다." if num<0 else "0입니다.")

print("양수입니다." if num>0 else "음수입니다.")
