N = sorted(list(map(int, input().split())))
S = list(input())

for i in range(3):
    S[S.index(chr(65 + i))] = N[i]

print(*S)