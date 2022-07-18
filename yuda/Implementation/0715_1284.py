import sys

num = [4, 2]
for _ in range(8):
    num.append(3)

while True:
    N = list(map(int, list(sys.stdin.readline().rstrip())))

    if len(N) == 1 and N[0] == 0:
        break

    result = 1
    for i in N:
        result += num[i] + 1
    print(result)