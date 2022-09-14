bx, by = map(int, input().split())
dx, dy = map(int, input().split())
jx, jy = map(int, input().split())

b = max(abs(bx - jx), abs(by - jy))
d = abs(dx - jx) + abs(dy - jy)
print("bessie" if b < d else "daisy" if b > d else "tie")