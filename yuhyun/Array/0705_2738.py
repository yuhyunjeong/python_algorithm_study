import sys

# 풀이 1
num = list(map(int, sys.stdin.readline().split()))
L = []

for i in range(num[0] * 2):
    L.append(list(map(int, sys.stdin.readline().split())))

for i in range(num[0]):
    for j in range(num[1]):
        print(L[i][j] + L[i + num[0]][j], end=" ")
    print()

# 풀이 2
num = list(map(int, sys.stdin.readline().split()))
L = []
result = [[0] * num[1] for _ in range(num[0])]

for i in range(num[0] * 2):
    L.append(list(map(int, sys.stdin.readline().split())))

for i in range(num[0]):
    for j in range(num[1]):
        result[i][j] = L[i][j] + L[i + num[0]][j]
    print(*result[i])