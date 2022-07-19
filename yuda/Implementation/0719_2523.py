N = int(input())
for i in range(1, N + 1):
    print("*" * i, sep="")
for i in range(1, N):
    print("*" * (N - i), sep="")