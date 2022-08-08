num = list(map(int, input().split()))
abc = list(input())

num.sort()

for i in abc:
    if i == "A":
        print(num[0], end=" ")
    elif i == "B":
        print(num[1], end=" ")
    else:
        print(num[2], end=" ")

# 풀이 2
N = sorted(list(map(int, input().split())))
S = list(input())

for i in range(3):
    S[S.index(chr(65 + i))] = N[i]

print(*S)



