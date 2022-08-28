cnt = 0
for i in range(int(input())):
    l, w, d, wt = map(float, input().split())
    flag = 0 if ((56 < l or 45 < w or 25 < d) and 125 < (l + w + d)) or 7 < wt else 1
    print(flag)
    cnt += flag
print(cnt)