l, r, a = map(int, input().split())
diff = max(l, r) - min(l, r)
if diff >= a:
    print((min(l, r) + a) * 2)
else:
    print((max(l, r) + ((a - diff) // 2)) * 2)