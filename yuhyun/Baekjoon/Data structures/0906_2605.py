n = int(input())
num = list(map(int, input().split()))
row = []

for i in range(n):
    row.insert(i-(num[i]), i+1)

print(*row)
