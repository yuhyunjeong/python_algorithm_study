import sys

N = int(input())
score = list(map(int, input().split()))
result = S = 0

for i in score:
    if i == 1:
        S += 1
        result += S
    else:
        S = 0

print(result)