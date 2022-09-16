skill = list(map(int, input().split()))
result = []
for _ in range(int(input())):
    score = 0
    for _ in range(3):
        team = list(map(int, input().split()))
        score += sum([s * t for s, t in zip(skill, team)])
    result.append(score)
print(max(result))