import sys

S = list(map(int, sys.stdin.readline().split()))
result = S[0] / S[1]

for _ in range(int(sys.stdin.readline())):
    T = list(map(int, sys.stdin.readline().split()))
    T = T[0] / T[1]
    if result > T:
        result = T

print("%.2f" % (result * 1000))