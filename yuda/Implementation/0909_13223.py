h, m, s = map(int, input().split(":"))
time1 = h * 3600 + m * 60 + s
h, m, s = map(int, input().split(":"))
time2 = h * 3600 + m * 60 + s

time = time2 - time1
if time <= 0: time += 24 * 3600
print(str(time // 3600).zfill(2), str(time % 3600 // 60).zfill(2), str(time % 60).zfill(2), sep=":")