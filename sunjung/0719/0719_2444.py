n = int(input())

for i in range(1, n+1): #range(시작숫자, 종료숫자, step)
    print(" "*(n-i) + "*"*(2*i-1))
for j in range(n-1,0,-1):
    print(" "*(n-j) + "*"*(2*j-1))