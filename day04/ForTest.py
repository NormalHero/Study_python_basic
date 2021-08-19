#ForTest.py
for i in range(10):
    print("Hello",i)

for i in range(1,11):
    print(i)

for i in range(10,0,-1):
    print(i)

#2부터 3씩 증가하며 10번반복
#2 5 8 11 14 17 20 23 26 29
for i in range(2,32,3):
    pass

for i in range(1,7,3):
    pass

#빠른 for문
arData = [10,20,30,40,50]

for i in range(5):
    print(i,arData[i])

for data in arData:
    print(data)
    
s = {1,2,3,4}
for  data in s:
    print(data)

d = {"fly":"날다", "work":"일하다", "run":"달리다"}
for key in d:
    print(d[key])

#"Hello", "Java", "C", "Python", "C++", "apple", "banana", "cherry"
#컬렉션은 규칙성이 없는 값에 규칙성을 부여하기 위해서 사용한다.
arMsg = ["Hello", "Java", "C", "Python", "C++", "apple", "banana", "cherry"]
for msg in arMsg:
    print(msg)






















