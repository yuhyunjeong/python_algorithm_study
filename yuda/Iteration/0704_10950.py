import sys

T = int(input())

for i in range(T):
    num = list(map(int, sys.stdin.readline().split()))
    print(sum(num))