score = [sum(list(map(int, input().split()))) for _ in range(5)]
M = max(score)
print(score.index(M) + 1, M)