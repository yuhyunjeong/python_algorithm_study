import sys


N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

cnt=0

for i in range(N) :    
    
    if num[i] == v :
        cnt += 1

print(cnt)

# print(num.count(v))