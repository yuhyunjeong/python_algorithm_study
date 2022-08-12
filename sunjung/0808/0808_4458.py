n = int(input())
for i in range(n) :
    a = input()
    print(a.capitalize())

#2번 풀이
for _ in range(int(input())):
    S = input()
    print(S[0].upper() + S[1:])

#3번 풀이
N = int(input())

for _ in range(N):
    str = input()

    # 풀이 1
    for i in range(len(str)):
        if i == 0:
            print(str[i].upper(),end='')
        else:
            print(str[i], end='')
    print()