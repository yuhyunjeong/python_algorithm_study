import sys

# 풀이 1
while True:
    try:
        print(input())
    except:
        break

# 풀이 2
str = sys.stdin.readlines()

for line in str:
    print(line.rstrip())