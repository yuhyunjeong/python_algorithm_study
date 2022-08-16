# sum(list(map(int, str(num)))) : 모든 자릿수의 합

while True :
    result = input()
    
    if result == '0':
        break

    while len(str(result)) > 1 :
        n = []
        for i in (result):
            n.append(int(i)) #각 자리수를 리스트에 추가

        result = str(sum(n))

    print(int(result))




""" 

while True:
    n = input()
    if n == '0':
        break
    while(len(n) > 1):
        li = list(map(int, n))
        n = str(sum(li))
    print(n)
 """