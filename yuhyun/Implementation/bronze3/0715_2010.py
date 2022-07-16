import sys


N = int(input())
result = 0

for _ in range(N) :
    num = int(sys.stdin.readline())
    result+=num

print(result-(N-1))



