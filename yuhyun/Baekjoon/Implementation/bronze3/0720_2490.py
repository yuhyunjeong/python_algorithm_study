for _ in range(3):
    yut = list(map(int,input().split()))

    if yut.count(0) == 1: #and yut.count(1) == 3:
        print('A')
    elif yut.count(0) == 2: #and yut.count(1) == 2:
        print('B')
    elif yut.count(0) == 3: #and yut.count(1) == 1:
        print('C')
    elif yut.count(0) == 4: #and yut.count(1) == 0:
        print('D')
    elif yut.count(0) == 0: #and yut.count(1) == 4:
        print('E')
    
# 풀이2
score = ['E', 'A', 'B', 'C', 'D']
N = 3
for i in range(N):
    result = list(map(int, input().split()))
    print(score[result.count(0)])