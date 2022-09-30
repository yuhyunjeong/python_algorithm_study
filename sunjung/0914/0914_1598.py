# 가로 - a-b/4
# 세로 - a-b
a, b = map(int, input().split())
a -= 1  # 0부터 시작하는 좌표, -1을 해준다.
b -= 1
print(abs(a//4 - b//4) + abs(a % 4 - b % 4))