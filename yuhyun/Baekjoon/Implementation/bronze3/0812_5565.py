N = list(int(input()) for _ in range(10))

result = N[0] - sum(N, -N[0])
print(result)    