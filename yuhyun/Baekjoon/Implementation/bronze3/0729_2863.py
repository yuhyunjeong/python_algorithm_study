a, b = map(int, input().split())
c, d = map(int, input().split())
f = []
f.append(a / c + b / d) # 0
f.append(c / d + a / b) # 1
f.append(d / b + c / a) # 2
f.append(b / a + d / c) # 3
f_max = max(f)
print(f.index(f_max))