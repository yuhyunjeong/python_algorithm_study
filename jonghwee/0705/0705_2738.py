import sys

N,M = map(int,sys.stdin.readline().split());

# matrix = [0 for _ in range(N)]
# for i in range(N):
#     matrix[i]=list(map(int,sys.stdin.readline().split()))

matrix1=[]
matrix2=[]
for i in range(N):
    matrix1.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    matrix2.append(list(map(int,sys.stdin.readline().split())))

print(matrix1);

print(matrix2);