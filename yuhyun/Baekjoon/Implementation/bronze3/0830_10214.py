t = int(input())

for _ in range(t):

    y_cnt = 0
    k_cnt = 0

    for i in range(9):
        y, k = map(int, input().split())

        y_cnt += y
        k_cnt += k

    if y_cnt > k_cnt:
        print("Yonsei")
    elif y_cnt < k_cnt:
        print("Korea")
    else:
        print("Draw")