import sys

T = int(sys.stdin.readline())

for _ in range(T):
    score = list(sys.stdin.readline().rstrip())
    result = 0
    S = 0

    for i in score:
        if i == 'O':
            S += 1
            result += S
        else:
            S = 0
    print(result)