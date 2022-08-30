for _ in range(int(input())):
    yonsei = korea = 0
    for _ in range(9):
        Y, K = map(int, input().split())
        yonsei += Y
        korea += K
    if yonsei > korea:
        print("Yonsei")
    elif korea > yonsei:
        print("Korea")
    else:
        print("Draw")