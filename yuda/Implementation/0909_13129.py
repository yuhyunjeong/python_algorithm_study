a, b, n = map(int, input().split())
result = []
for i in n:
    result.append(a * n + b * (i + 1))
print(*result)