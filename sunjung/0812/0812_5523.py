from sys import stdin

a_score=0
b_score=0

for _ in range (int(stdin.readline())) :
    a,b = map(int, stdin.readline().split())
    if a>b :
        a_score += 1
    elif a<b :
        b_score += 1

print(a_score,b_score)

# 풀이2
import sys

result = [0] * 2
for _ in range(int(input())):
    A, B = map(int, sys.stdin.readline().split())
    result[0] += A > B
    result[1] += A < B
print(*result)