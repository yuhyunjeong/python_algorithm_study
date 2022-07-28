# 최댓값 찾고 위치 찾기
import sys

X = 1 #행
Y = 1 #열
Max = 0 #최댓값

board = [] #한줄

for i in range(1,10) : #1~9까지 (9*9격자판)
     board = list(map(int,sys.stdin.readline().split()))
     if(Max<max(board)): #기존 최댓값 < 매 행 최대값
        Max = max(board)
        X=i
        Y=board.index(Max)+1

print(Max)
print(X,Y) #Y는 인덱스, +1 해준다

