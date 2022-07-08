# 풀이 1
time = list(map(int, input().split()))

time[1] -= 45
if time[1] < 0:
    time[1] += 60
    time[0] -= 1
    if time[0] < 0:
        time[0] += 24

print(*time)

# 풀이 2
time = list(map(int, input().split()))

time[0] += (time[1] - 45) // 60
time[1] = (time[1] - 45) % 60
if time[0] < 0:
    time[0] += 24

print(*time)