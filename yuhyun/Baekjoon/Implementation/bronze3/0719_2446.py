# 출력형식오류 : 불필요한 공백 없어야함

N = int(input())

for i in range(N):
    print(" "*(i)+"*"*(N-i+N-i-1))
for i in range(N-1):
    print(" "*(N-i-2)+"*"*(i+1+i+1+1))