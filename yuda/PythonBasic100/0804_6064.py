num = list(map(int, input().split()))
print(min(num))
print((num[0] if num[0] < num[1] else num[1]) if num[0] < num[2] and num[1] < num[2] else num[2])