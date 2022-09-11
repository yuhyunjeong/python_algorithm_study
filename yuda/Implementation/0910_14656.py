n = int(input())
num = list(map(int, input().split()))
count = 0
for i in range(n):
    if i + 1 != num[i]:
        count += 1
print(count)