from sys import stdin

x = []
y = []

n = int(input())
for _ in range (n) :
    a,b = map(int, stdin.readline().split())
    x.append(a)
    y.append(b)

print((max(x)-min(x))*(max(y)-min(y)))

