n = int(input())
a = list(map(int, input().split()))

a.sort()

num = 1

for i in a:
    if num == i:
        num+=1

print(num)
