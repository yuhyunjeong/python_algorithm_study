# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 
# 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. 
# N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다

n, m = map(int, input().split())
a, b = [], []
for i in [a, b]:
    for j in range(n):
        i.append(list(map(int, input().split()))) #append는 기존 리스트에 값을 추가, 마지막 위치에 값이 들어간다
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
    print(*a[i])

#--------------------------------------------------------

n, m = map(int, input().split())
a = []

for _ in range(n):
    a.append((list(map(int, input().split()))))

for i in range(n):
    b = list(map(int, input().split()))

    for j in range(m):
        a[i][j] += b[j]

for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()