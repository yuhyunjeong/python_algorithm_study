for _ in range(int(input())):
    n, i = map(int, input().split())
    print("Valid" if bin(n)[2:].count("1") % 2 == i else "Corrupt")