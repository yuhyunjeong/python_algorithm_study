n, m, k = map(int, input().split())
flag = 1
if k < 3:
    flag = -1
for _ in range(3, k, flag):
    m += flag
    if m > n:
        m = 1
    if m < 1:
        m = n
    print(m)
print(m)