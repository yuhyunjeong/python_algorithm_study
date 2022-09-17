# Python - 시간초과 / pypy3으로 제출

for _ in range(int(input())):

    n, m = map(int, input().split())
   
    pair = [0, 0]
    cnt = 0

    for i in range(1,n):

        pair[0] = i
        for j in range(i+1,n):

            pair[1] = j
            num = (pair[0]**2 + pair[1]**2 + m) / (pair[0]*pair[1])
 
            if int(num) == num:
                cnt += 1
    
    print(cnt)
