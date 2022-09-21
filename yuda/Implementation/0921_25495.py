n = int(input())
a = list(map(int, input().split()))
result = somo = 2
for i in range(1, n):
    if a[i - 1] == a[i]:
        somo *= 2
    else:
        somo = 2
    result += somo
    if result >= 100:
        result = 0
        somo = 1
print(result)