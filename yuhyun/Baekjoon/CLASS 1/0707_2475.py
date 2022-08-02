import sys


num = list(map(int, sys.stdin.readline().split()))
sum = 0 
result = 0

for i in num :
    sum += i**2

result = sum % 10
print(result)

# 풀이 2
num = [i**2 for i in map(int,input().split())]
print(sum(num) % 10)