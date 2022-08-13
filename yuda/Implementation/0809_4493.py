# 풀이 1
rps = {"R":"P", "P":"S", "S":"R"}

for _ in range(int(input())):
    result = {1:0, 2:0}

    for i in range(int(input())):
        P1, P2 = input().split()
        if rps[P1] == P2:
            result[2] += 1
        elif rps[P2] == P1:
            result[1] += 1

    if result[1] > result[2]:
        print("Player 1")
    elif result[1] < result[2]:
        print("Player 2")
    else:
        print("TIE")