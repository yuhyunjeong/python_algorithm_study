n = int(input())
print(n)
result = [i for i in range(1, n - 1)]
result.append(53)
print(*result)