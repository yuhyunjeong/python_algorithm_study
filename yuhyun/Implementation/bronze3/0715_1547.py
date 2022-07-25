M = int(input())

num=[1, 2, 3]

for _ in range(M):
    X, Y = map(int, input().split())
    
    num[X-1] , num[Y-1] = num[Y-1] , num[X-1]

print(num.index(1)+1)


