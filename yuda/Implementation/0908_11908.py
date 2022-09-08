n = int(input())
num = sorted(list(map(int, input().split())))
print(sum(num[:n - 1]))