t = int(input())

money = [25, 10, 5, 1] # 100센트 = 1달러
cnt = [0]*4

for _ in range(t):

    c = int(input())

    for i in range(len(money)):
        
        cnt[i] = c // money[i]

        c = c % money[i]
    
    print(*cnt)