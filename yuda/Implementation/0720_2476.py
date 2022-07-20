import sys

N = int(sys.stdin.readline())
score = []

for i in range(N):
    dice = sorted(list(map(int, sys.stdin.readline().split())))
    if dice[0] == dice[2]:
        score.append(10000 + dice[0] * 1000)
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        score.append(1000 + dice[1] * 100)
    else:
        score.append(max(dice) * 100)

print(max(score))