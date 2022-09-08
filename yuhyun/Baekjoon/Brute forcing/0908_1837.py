P, K = map(int, input().split())
a = True
for i in range(2,K): # P에 K보다 작은 소인수가 있는지 확인
    if P % i == 0:
        print('BAD',i)
        a = False
        break
if a:
    print('GOOD')
