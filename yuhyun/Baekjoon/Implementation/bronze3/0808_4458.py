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

    # 풀이 2
    strOne = str[0].upper()

    str = strOne + str[1: ]
    print(str)