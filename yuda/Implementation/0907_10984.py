for _ in range(int(input())):
    C = G = 0
    for _ in range(int(input())):
        c, g = map(float, input().split())
        C += c
        G += c * g
    print(int(C), round(G / C, 1))