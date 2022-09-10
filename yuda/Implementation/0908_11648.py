n = int(input())
i = 0
while n > 9:
    n = list(map(int, str(n)))
    multi = 1
    for j in n:
        multi *= j
    n = multi
    i += 1
print(i)