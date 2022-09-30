max_s = [100, 100, 200, 200, 300, 300, 400, 400, 500]
score = list(map(int, input().split()))

for m, s in zip(max_s, score):
    if s > m:
        print("hacker")
        exit()
print("draw" if sum(score) > 99 else "none")