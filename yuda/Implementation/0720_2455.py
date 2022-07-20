import sys

P = []
for i in range(4):
    now = list(map(int, sys.stdin.readline().split()))
    if len(P) == 0:
        P.append(now[1])
    else:
        P.append(P[i - 1] - now[0] + now[1])
print(max(P))