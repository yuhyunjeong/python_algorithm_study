n = int(input())  # 과목 수
score = list(map(int, input().split())) #현재성적
max = max(score)

for i in range(n) :
    score[i] = score[i] / max * 100
print(sum(score) / n)
