import sys

result = [0] * 2
for _ in range(int(input())):
    A, B = map(int, sys.stdin.readline().split())
    result[0] += A > B
    result[1] += A < B
print(*result)