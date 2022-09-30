n = int(input())
for _ in range(n):
    print("@" * (n + n * 4))
for _ in range(n * 4):
    print("@" * n)