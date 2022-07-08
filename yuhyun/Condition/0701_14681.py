import sys


x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
num = 0

if x > 0 and y > 0 :
    num = 1
elif x < 0 and y > 0 :
    num = 2
elif x < 0 and y < 0 :
    num = 3
elif x > 0 and y < 0 :
    num = 4

print(num)