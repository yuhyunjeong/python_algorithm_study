n = int(input())
for _ in range(n * 2):
    print("@" * n + " " * (3 * n) + "@" * n)
for _ in range(n):
    print("@" * (n + n * 4))
for _ in range(n):
    print("@" * n + " " * (3 * n) + "@" * n)
for _ in range(n):
    print("@" * (n + n * 4))