import sys


N = int(input())

A = B = 0

for _ in range(N):
    
    a, b = map(int, sys.stdin.readline().split())

    if a == b:
        continue
    elif a > b :
        A += 1
    elif a < b:
        B += 1

print(A,B)

# 풀이 2
import sys

result = [0] * 2
for _ in range(int(input())):
    A, B = map(int, sys.stdin.readline().split())
    result[0] += A > B
    result[1] += A < B
print(*result)
