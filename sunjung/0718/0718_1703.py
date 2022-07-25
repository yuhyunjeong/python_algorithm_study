while True:
    li = list(map(int, input().split()))
    leaf = 1 #구하려는 나뭇잎 수

    if li[0] == 0: #0 입력시 종료
        break

    for i in range(1, len(li), 2): #range(시작숫자, 종료숫자, step)
        leaf = leaf * li[i] - li[i+1]

    print(leaf)