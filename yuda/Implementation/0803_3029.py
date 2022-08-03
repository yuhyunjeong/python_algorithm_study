# 풀이 1
H1, M1, S1 = map(int, input().split(":"))
H2, M2, S2 = map(int, input().split(":"))
H = H2 - H1
M = M2 - M1
S = S2 - S1
if S < 0:
    M -= 1
    S += 60
elif S >= 60:
    M += 1
    S -= 60
if M < 0:
    H -= 1
    M += 60
elif M >= 60:
    H += 1
    M -= 60
if H < 0:
    H += 24
if H + M + S == 0:
    H = 24
print("{0:0>2}:{1:0>2}:{2:0>2}".format(H, M, S))

# 풀이 2
time1 = list(map(int, input().split(":")))
time2 = list(map(int, input().split(":")))
time = 0
for i in range(3):
    time += (time2[i] - time1[i]) * (60 ** (2 - i))
if time <= 0:
    time += 24 * (60 ** 2)
print("{0:0>2}:{1:0>2}:{2:0>2}".format(time // 3600, time % 3600 // 60, time % 3600 % 60))