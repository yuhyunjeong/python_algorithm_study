n, t = map(int, input().split())
task = list(map(int, input().split()))
for i in range(n):
    if t - task[i] < 0:
        print(i)
        exit()
    else:
        t -= task[i]
print(i + 1)