import sys


x, y = map(float, sys.stdin.readline().split())

N = int(input())
lst = [x*1000/y]

for i in range(N):
    I = list(map(float, sys.stdin.readline().split()))
    lst.append(I[0]*1000/I[1])

print(format(min(lst), ".2f"))

