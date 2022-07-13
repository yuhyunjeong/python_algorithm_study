import sys

list=[]
remainder=[]
for i in range(10):
    list.append(int(sys.stdin.readline().rstrip()))

for i in range(0,len(list)):
    remainder.append(list[i]%42)

#풀이 2
list = []
for i in range(10) : 
    n = int(input())
    list.append(n%42)
list=set(list) #set()을 이용하면 중복된 값을 제거한다
print(len(list)) #list길이 구하기

#풀이 3
result = set()

for _ in range(10):
    result.add(int(sys.stdin.readline()) % 42)

print(len(result))