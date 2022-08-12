# 풀이 1
n = int(input())
for _ in range(9):
    n -= int(input())
print(n)

# 풀이 2
print(int(input()) - sum([int(input()) for i in range(9)]))