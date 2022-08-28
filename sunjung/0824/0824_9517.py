# 게임이 시작한지 3분 30초(210초) 가 지나면 터지는 폭탄

k = int(input()) 
n = int(input()) 
time = 0

for _ in range(n) :
    t,z = input().split() #시간, 대답(T,P,N)
    t = int(t) #시간은 int타입으로 변환
    
    time += t #질문 대답하는데 걸리는 시간 더해준다

    #210초 지나면(이상이면) 폭탄 터짐
    if (time>=210) :
        print(k)
        break

    #정답이 맞으면, 다음사람(k+1)에게 문제 토스
    if z =='T':
        k += 1
        if k == 9 : #플레이어는 총8명
            k = 1   #다시 1번으로 초기화 해준다

    