from sys import stdin

n = int(input()) # 조사한 시간
m = int(input()) # 조사를 시작할 때, 터널 안에 들어있는 차량의 수
result = [m]

for i in range (n) :
    a,b = map(int, stdin.readline().split()) #입구를 통과한 차의 수와 출구를 통과한 차의 수
    c = m + (a-b) #a-b:터널 안에 있는 차량의 수
    result.append(c)
    m = c

if min(result) < 0 :
    print(0)
else :
    print(max(result))




#풀이2
""" n = int(input())
m = [int(input())]
for i in range(n):
    I, O = map(int, input().split())
    s = m[i] + I - O
    if s < 0:
        print(0)
        exit()
    else:
        m.append(s)
print(max(m)) """