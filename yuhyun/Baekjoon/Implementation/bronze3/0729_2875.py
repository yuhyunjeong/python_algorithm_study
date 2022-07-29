import sys


n, m, k = map(int, sys.stdin.readline().split())
result = 0

while n >= 2 and m >= 1 and n + m >= k + 3:	# 2명 , 1명 팀 만들 수 있고, 인턴쉽도 보낼 수 있는 수 일때
    n -= 2	# 빼주고
    m -= 1	# 빼주고
    result += 1	# 팀 수는 하나씩 더해준다
print(result)

from math import ceil

# 풀이 1
N, M, K = map(int, input().split())
team = min(N // 2, M)
T = (N - (team * 2)) + (M - team)
intern = max(K - T, 0)
team -= ceil(intern / 3)
print(team)

# 풀이 2
N, M, K = map(int, input().split())
print(min(N // 2, M, (N + M - K) // 3))

# 풀이 3
N, M, K = map(int, input().split())
team = 0
while N + M - K >= 3 and N >= 2 and M >= 1:
    N -= 2
    M -= 1
    team += 1
print(team)