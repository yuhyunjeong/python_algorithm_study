n, min_m, max_m, t, r = map(int, input().split())
m = min_m
result = 0
if m + t > max_m:
    print(-1)
    exit()
while n != 0:
    if max_m >= m + t:
        m += t
        n -= 1
    elif m + t > max_m:
        m = max(m - r, min_m)
    result += 1
print(result)