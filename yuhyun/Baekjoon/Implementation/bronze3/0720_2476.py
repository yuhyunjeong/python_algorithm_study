N = int(input())
money = []

for _ in range(N):
    a, b, c = map(int, input().split())
    result = 0

    if a == b == c :
        result = 10000+(a*1000)
    elif a == b :
        result = 1000 + (a*100)
    elif b == c :
        result = 1000 + (b*100)
    elif c == a :
        result = 1000 + (c*100)
    else:
        result = max(a,b,c) * 100
    money.append(result)

print(max(money))

# 풀이 2
import sys

N = int(sys.stdin.readline())
score = []

for i in range(N):
    #오름차순정렬
    dice = sorted(list(map(int, sys.stdin.readline().split()))) 
    if dice[0] == dice[2]:
        score.append(10000 + dice[0] * 1000)
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        score.append(1000 + dice[1] * 100)
    else:
        score.append(max(dice) * 100)

print(max(score))