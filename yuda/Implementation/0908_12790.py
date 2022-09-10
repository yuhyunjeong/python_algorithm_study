for _ in range(int(input())):
    n = list(map(int, input().split()))
    HP = max(n[0] + n[4], 1)
    MP = max(n[1] + n[5], 1)
    GG = max(n[2] + n[6], 0)
    BE = n[3] + n[7]
    print(1 * HP + 5 * MP + 2 * GG + 2 * BE)