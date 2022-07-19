# 풀이 1
N = int(input())
for i in range(N, 0, -1):
    print(" " * (N - i), "*" * (2 * i - 1), sep="")

# 풀이 2
N = int(input())
for i in range(N):
    print(" " * i, "*" * (2 * (N - i) - 1), sep="")