
n = int(input())
result = []

for _ in range(n) :
    a, b, c = map(int, input().split())

    if a==b==c :
        result.append(10000 + a * 1000)
    elif a == b :
        result.append(1000 + a * 100)
    elif a == c :
        result.append(1000 + a * 100)
    elif b == c :
        result.append(1000 + b * 100)
    else :
        result.append(max(a, b, c) * 100) #a,b,c중 최댓값 *100

print(max(result))

#2번째 풀이
import sys

N = int(sys.stdin.readline())
score = []

for i in range(N):
    dice = sorted(list(map(int, sys.stdin.readline().split()))) #sorted 오름차순 정렬
    if dice[0] == dice[2]:
        score.append(10000 + dice[0] * 1000)
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        score.append(1000 + dice[1] * 100)
    else:
        score.append(max(dice) * 100)

print(max(score))


