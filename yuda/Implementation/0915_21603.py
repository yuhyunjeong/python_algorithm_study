n, k = map(int, input().split())
result = [i for i in range(1, n + 1) if str(i)[-1] != str(k)[-1] and str(i)[-1] != str(2 * k)[-1]]
print(len(result))
print(*result)