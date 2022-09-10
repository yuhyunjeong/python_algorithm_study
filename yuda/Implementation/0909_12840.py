h, m, s = map(int, input().split())
time = h * 3600 + m * 60 + s
for _ in range(int(input())):
    n = input()
    if n == "3":
        print(time // 3600, time % 3600 // 60, time % 60)
    else:
        n = list(map(int, n.split()))
        if n[0] == 1:
            time += n[1]
        else:
            time -= n[1]
        time %= 24 * 3600