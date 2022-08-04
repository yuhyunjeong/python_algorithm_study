num = [i for i in list(map(int, input().split())) if i % 2 == 0]
print(*num, sep="\n")