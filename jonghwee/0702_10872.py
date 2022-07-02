import sys

N = int(sys.stdin.readline());
result = 1;

for i in range(1,N+1,1) : #range(start,stop,증감값) -> 이 때 stop에 들어가는 숫자 바로 전에 끝나기 때문에 N+1 까지 해줘야 N까지 계산한다.
    result *= i

print(result);