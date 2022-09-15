# 풀이 1
n, x, k = map(int, input().split())
for _ in range(k):
    a, b = map(int, input().split())
    if a == x:
        x = b
    elif b == x:
        x = a
print(x)

# 풀이 2
n, x, k = map(int, input().split())
result = [0] * (n + 1)
result[x] = 1
for _ in range(k):
    a, b = map(int, input().split())
    result[a], result[b] = result[b], result[a]
print(result.index(1))