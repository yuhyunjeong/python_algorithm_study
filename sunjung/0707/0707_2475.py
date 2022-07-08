import sys

sum = 0
for n in list(map(int,input().split())) :
    sum += n**2
print(sum%10)

# 풀이2
num = [i ** 2 for i in map(int, input().split())]
print(sum(num) % 10)