#Split.py
a,b,c="10,20,30".split(",")
#print(a)
#print(b)
#print(c)

                            #int("10""20") ---> (X)
num1,num2 = input("두 정수를 입력하세요(예 : 10,20) : ").split(",")
num1 = int(num1)
num2 = int(num2)
print(num1+num2)
