import sys


n = int(sys.stdin.readline()) # 시간초과 방지
lst = []

for i in range(n):
    h = int(sys.stdin.readline())
    lst.append(h)

last = lst[-1]
cnt = 1

for i in range(n-1,-1,-1): # for문 거꾸로 반복 / for i in reversed(range(n)) 은 시간초과
    if lst[i] > last:
        cnt += 1
        last = lst[i] # 비교할 숫자 갱신
print(cnt)

