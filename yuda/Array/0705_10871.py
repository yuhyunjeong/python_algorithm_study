# 풀이 1
num = list(map(int, input().split()))
lst = list(map(int, input().split()))

for i in range(num[0]):
    if lst[i] < num[1]:
        print(lst[i], end=" ")

# 풀이 2
num = list(map(int, input().split()))
lst = list(map(int, input().split()))
result = []

for n in lst:
    if n < num[1]:
        result.append(n)

print(*result)

# 풀이 3
num = list(map(int, input().split()))
result = [i for i in map(int, input().split()) if i < num[1]]

print(*result)