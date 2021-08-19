#ListTest.py
'''
dataList = [10,20,30,40,50]

dataList[1] = 200
print(dataList[1])
'''
#빈 리스트 만들기
dataList = list()

dataList.append(10) #[10]
dataList.insert(0,20) #[20,10]
#len(리스트명) : 리스트의 요소 개수
dataList.insert(len(dataList),30) #[20,10,30]

#간단하게 리스트의 구조 확인하기
print(dataList)

#리스트의 요소 삭제하기
data = dataList.pop() #[20,10]
print(data)
print(dataList)
dataList.remove(20) #[10]
print(dataList)
del dataList[0] #[]
#del dataList
print(dataList)



















