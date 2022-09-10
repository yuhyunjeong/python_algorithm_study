CY = SD = 100
for _ in range(int(input())):
    c, s = map(int, input().split())
    if c > s:
        SD -= c
    elif s > c:
        CY -= s
print(f"{CY}\n{SD}")