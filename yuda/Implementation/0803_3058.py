import sys

T = int(sys.stdin.readline())

for _ in range(T):
    num = [i for i in list(map(int, sys.stdin.readline().split())) if i % 2 == 0]
    print(sum(num), min(num))