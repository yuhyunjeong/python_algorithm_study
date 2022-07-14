import sys


T = int(sys.stdin.readline().rstrip()); #.rstrip()은 문자가 들어갈 경우 넣어주면 좋음. 앞에 int()가 붙으면 자동으로 개행문자 떨어짐.
for i in range(1,T+1,1):
    A,B = map(int, sys.stdin.readline().split());
    print(A+B);