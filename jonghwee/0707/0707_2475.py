import sys

num = list(map(int,sys.stdin.readline().split()));
for i in range(len(num)):
    num[i] = num[i]**2

print(sum(num)%10)

#풀이 2
sum=0
for n in list(map(int,input().split())):
    sum += n**2
print(sum%10)

#풀이 3
num = [i ** 2 for i in map(int, input().split())]
print(sum(num)%10)