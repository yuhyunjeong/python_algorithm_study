from math import ceil

n,m,k = map(int, input().split()) #여학생,남학생,참여해야하는 인원

# 풀이 1
# N, M, K = map(int, input().split())
# team = min(N // 2, M)
# T = (N - (team * 2)) + (M - team)
# intern = max(K - T, 0)
# team -= ceil(intern / 3)
# print(team)

# 풀이 2
# N, M, K = map(int, input().split())
# print(min(N // 2, M, (N + M - K) // 3))

# 풀이 3
N, M, K = map(int, input().split())
team = 0
while N + M - K >= 3 and N >= 2 and M >= 1:
    N -= 2
    M -= 1
    team += 1
print(team)