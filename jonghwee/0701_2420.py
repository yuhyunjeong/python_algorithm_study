import sys

N,M = map(int,sys.stdin.readline().split());
#num, = list(map(int,input().split())) -> 다수의 수를 넣을 때는 list가 유용하게 쓰일 수 있다.
# result = num[0]-num[1]
# if문 써서 result가 음수일 때는 -1을 곱해서, 양수일 때는 그냥 출력되도록 나눠서 계산할수도 있음.
print(abs(N-M));
