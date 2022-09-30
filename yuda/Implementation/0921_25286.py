month = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
for _ in range(int(input())):
    y, m = map(int, input().split())
    if ((y % 100 != 0 and y % 4 == 0) or y % 400 == 0) and m == 3:
        print(y, 2, 29)
    elif m == 1:
        print(y - 1, 12, 31)
    else:
        print(y, m - 1, month[m])