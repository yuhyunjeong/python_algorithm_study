n = int(input())
for _ in range(n):
    print("@" * (n + n * 4))
for _ in range(n * 3):
    print("@" * n + " " * (3 * n) + "@" * n)
for _ in range(n):
    print("@" * (n + n * 4))