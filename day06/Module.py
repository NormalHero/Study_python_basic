#Module.py
#원소 in 컬렉션 : 실제로 해당 원소가 컬렉션 안에 있으면 참
#"10+3" : 13
def calc(eq):
    result = 0
    if '+' in eq:
        datas = eq.split('+')
        result = int(datas[0]) + int(datas[1])
    elif '-' in eq:
        datas = eq.split('-')
        result = int(datas[0]) - int(datas[1])
    elif '*' in eq:
        datas = eq.split('*')
        result = int(datas[0]) * int(datas[1])
    elif '/' in eq:
        datas = eq.split('/')
        result = int(datas[0]) / int(datas[1])
    return result

#print(calc("10-3"))















