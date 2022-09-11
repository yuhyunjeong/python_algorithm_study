scores = []
for _ in range(int(input())):
    scores.append(list(map(int, input().split())))

win = sorted(scores, key = lambda x:(-x[0], x[1], x[2]))
print(scores.index(win[0]) + 1)