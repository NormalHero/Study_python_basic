#ReadTest.py
try:
    #file = open("djdmdmdkd.txt","r")
    file = open("test.txt","r")
    lines = file.readlines()
    print(lines)
    for line in lines:
        #"문자열1".rstrip("문자열2") : 문자열1의 오른쪽에 문자열2가 있다면 제거한 후 리턴
        print(line.rstrip("\n"))
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
