import sys

T = int(input())
for i in range (T):
        A,B= map(int,sys.stdin.readline().split())
        print(A+B)

#sys.stdin.readline().rstrip() 마지막 개행문자를 떼준다. 문자 입력받을때 좋다!