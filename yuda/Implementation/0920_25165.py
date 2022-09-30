n, m = map(int, input().split())
a, d = map(int, input().split())
x, y = map(int, input().split())

result = "NO..."
if (x == 1 and y < a) or (x == n and m % 2 != d):
    result = "YES!"
print(result)