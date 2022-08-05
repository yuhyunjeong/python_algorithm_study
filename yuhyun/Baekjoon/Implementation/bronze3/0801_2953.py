# 풀이 1
score = [sum(list(map(int, input().split()))) for _ in range(5)]
M = max(score)
print(score.index(M) + 1, M)

# 풀이 2
total = []
for _ in range(5):
    score = list(map(int,input().split(' ')))
    total.append(sum(score)) 

print(total.index(max(total))+1,max(total))