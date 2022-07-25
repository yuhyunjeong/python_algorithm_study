import sys


num = list(map(int, sys.stdin.readline().split()))

news_num = list(map(int, sys.stdin.readline().split()))

result = [i - (num[0]*num[1]) for i in news_num]

print(*result)

# 풀이 2

l, p = map(int, input().split())
cnt = list(map(int, input().split()))
party = l * p
for i in cnt:
    print(i - party, end=' ') # 개행 대신 공백