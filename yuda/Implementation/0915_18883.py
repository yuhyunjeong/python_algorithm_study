n, m = map(int, input().split())
for i in range(n):
    print(*[i * m + j for j in range(1, m + 1)])