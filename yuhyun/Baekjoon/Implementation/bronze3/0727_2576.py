odd = 0
cnt_odd = []

for _ in range(7):
    N = int(input().strip()) #개행문자 기준

    if N % 2 != 0 :
        odd += N
        cnt_odd.append(N)

if len(cnt_odd)==0: # 홀수가 없는 경우
    print(-1)
else:
    print(odd)
    print(min(cnt_odd))


