num = sorted(list(map(int, input().split())))
if num[0] + num[2] == num[1] * 2:
    print(num[2] + num[1] - num[0])
else:
    print(num[2] + num[0] - num[1])