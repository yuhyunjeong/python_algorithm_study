score = ['E', 'A', 'B', 'C', 'D']
N = 3
for i in range(N):
    result = list(map(int, input().split()))
    print(score[result.count(0)])