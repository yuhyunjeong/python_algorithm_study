N = [list(map(int, input().split())) for _ in range(9)]

result = 0
row = column = 1

for i in range(len(N)):
    if result < max(N[i]):
        result = max(N[i])
        row = i + 1
        column = N[i].index(result) + 1

print(result)
print(row, column)