while True:

    b, n = map(int, input().split())

    if n == 1: print(b); continue # n 이 1 일때는 B = A

    if b == n == 0:
        break
    
    a = [-1, 1e9] # 1e9 : 최댓값이 10억 미만일때 , 10**9

    for i in range(1,1001): # N = 2일 때 B = 1,000,000인 경우는 A = 1,000

        if a[1] > abs(b - i**n):
            a = [i, abs(b - i**n)]

    print(a[0])

        

        