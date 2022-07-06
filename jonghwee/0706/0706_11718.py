import sys

#풀이1
str = sys.stdin.readlines();
for line in str:
    print(line.rstrip())

#풀이2
while True:
    try:
        print(input())
    except:
        break;