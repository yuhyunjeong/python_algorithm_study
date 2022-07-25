n = int(input())

for i in range(1, n+1): #range(시작숫자, 종료숫자, step) 9-7-5-3-1-3-5-7-9
    print(" "*(i-1)+"*"*(2*(n-i) + 1))

for j in range(1,n):
    print(" "*(n-j-1)+"*"*((2*j) + 1)) #3-5-7-9