for _ in range(int(input())):
    d = int(input())
    t = 0
    while (t + 1) ** 2 + t + 1 <= d:
        t += 1
    print(t)