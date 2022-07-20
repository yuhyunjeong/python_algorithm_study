import sys

P = []
for i in range(10):
    now = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        P.append(now[1])
    else:
        P.append(P[i - 1] - now[0] + now[1])
print(max(P))