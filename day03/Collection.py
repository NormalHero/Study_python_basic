#Collection.py
'''
#컬렉션들 끼리는 형변환이 가능하다.
#list, tuple, set
li = [1,1,1,2,3,4,1,1,3,2,4,1,3,2,2,2,1,3,1,3,2,3,4,1,3,1,3,2,3,4,1,3,2]
s = set(li)
print(s)
'''
s = set()
#셋에 요소 추가하기
s.add(1)                #하나의 값 추가하기
s.update([2,3,4])       #여러개의 값 추가하기
print(s)
#셋에서 요소 삭제하기
s.remove(2)             #셋에서 요소 삭제하기
print(s)
#셋에서 요소를 가져올 때는 list나 tuple로 형변환을 한 후 그것에서 방번호로 접근한다.
li = list(s)
print(li[1])
#합집합(셋1|셋2)     #교집합(셋1&셋2)     #차집합(셋1-셋2)

#dict
d = {"하나":1, "둘":2, "셋":3, "넷":4, "다섯":5}
print(d["하나"])  #1

#.keys() 메소드가 반환하는 컬렉션은 list가 아니다.
#따라서 반환받은 컬렉션에서 방번호로 접근하려면 list로 형변환 후 사용한다.
keys = list(d.keys())
print(keys[1])

values = list(d.values())
print(values[4])

#.items() : 키, 값을 동시에 관리하고 싶을 때 사용
items = list(d.items())
print(items[0][0])


















