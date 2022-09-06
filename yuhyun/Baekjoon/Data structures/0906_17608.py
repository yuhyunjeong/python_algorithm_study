n = int(input())
lst = []

for i in range(n):
    h = int(input())
    lst.append(h)

last = lst[-1]
cnt = 1

for i in reversed(range(n)): # for문 거꾸로 반복
    if lst[i] > last:
        cnt += 1
        last = lst[i] # 비교할 숫자 갱신
print(cnt)

