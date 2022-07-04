import sys

# 예외 처리 방법
while True:
    try:
        n = list(map(int, input().split()))
        print(sum(n))
    except:
        break

# readlines() 사용
lines = sys.stdin.readlines()
for line in lines:
    num = list(map(int,line.split()))
    print(sum(num))