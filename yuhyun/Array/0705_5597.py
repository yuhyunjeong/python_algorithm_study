import sys

lst = list(range(1,31)) # range로 리스트 만들기

for i in range(28) :
    num = int(sys.stdin.readline())
    lst.remove(num)

for i in lst :
    print(i) # 리스트 요소 출력





# set의 차집합
result = [i for i in range(1, 31)]
sukje = []

while len(sukje) < 28:
    sukje.append(int(input()))
else:
    result = list(set(result).difference(sukje))
    print(min(result))
    print(max(result))