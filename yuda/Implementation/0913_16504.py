# 풀이 1
n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
result = 0
for n in num:
    result += sum(n)
print(result)

# 풀이 2
n = int(input())
num = [sum(map(int, input().split())) for _ in range(n)]
print(sum(num))