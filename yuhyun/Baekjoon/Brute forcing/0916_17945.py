a, b = map(int, input().split())
lst = []

for x in range(-1000,1001):
    if x**2 + 2*a*x + b == 0:
        lst.append(x)
print(*lst)