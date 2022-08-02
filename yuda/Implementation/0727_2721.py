import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(sum([i * sum(range(i + 2)) for i in range(1, n + 1)]))

T = int(input()) #테스트 케이스의 수
for _ in range(T) :
    n = int(input())

    sum = 0
    t = 0 #삼각수의 합
    for i in range(1, n+1): #1~n까지       1~3
        for j in range(1, i+2): #1~n+1까지  1~4
            t += j 
        sum += i * t
        t = 0 #더하고 다시 초기화
    print(sum)