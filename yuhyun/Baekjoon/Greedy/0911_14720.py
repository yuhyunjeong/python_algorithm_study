n = int(input())

milk = list(map(int, input().split()))

cnt = 0

for i in range(n):
    
    # if milk[i] == i % 3 : 중간에 연속하지 않았는데 성립하는 경우가 생길 수 있다

    if milk[i] == cnt % 3: # 0 1 2 0 1 2 반복이므로
        cnt += 1

print(cnt)
    
