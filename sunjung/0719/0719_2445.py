n = int(input())

for i in range(1, n): #range(시작숫자, 종료숫자, step)
    print("*"*i+" "*(2*(n-i))+"*"*i)
for j in range(n,0,-1):
    print("*"*j+" "*(2*(n-j))+"*"*j)
