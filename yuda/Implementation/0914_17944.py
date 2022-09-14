# 풀이 1: 시뮬레이션
n, t = map(int, input().split())
result = 1
flag = True
for _ in range(t - 1):
    if flag:
        result += 1
    else:
        result -= 1
    if result == 1 or result == 2 * n:
        flag = not flag
print(result)

# 풀이 2: 계산
n, t = map(int, input().split())
result = (t - 1) % (4 * n - 2) + 1
if result > 2 * n:
    result = (4 * n) - result
print(result)