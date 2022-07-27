# 풀이 1
num = [int(input()) for _ in range(7)]

M = 100
result = 0
for i in num:
    if i % 2 == 1:
        result += i
        M = min(M, i)

if result == 0:
    print(-1)
else:
    print(result)
    print(M)

# 풀이 2
odd = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        odd.append(num)

if len(odd) == 0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))