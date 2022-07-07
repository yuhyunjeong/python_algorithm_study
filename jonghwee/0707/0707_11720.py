import sys

N=int(sys.stdin.readline());
a=input();

sum=0

for i in a:
    sum += int(i)
print(sum)

#풀이2
n = input()
print(sum(map(int,input())))