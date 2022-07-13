list = []
for i in range(10) : 
    n = int(input())
    list.append(n%42)
list=set(list) #set()을 이용하면 중복된 값을 제거한다
print(len(list)) #list길이 구하기

#풀이2

import sys

result = set()
for _ in range(10):
    result.add(int(sys.stdin.readline()) % 42)
print(len(result))