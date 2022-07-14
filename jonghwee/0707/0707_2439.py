N = int(input())

for i in range(1,N+1):
    print(" "*(N-i),"*"*i,sep="")

#풀이 2
n = int(input())

for i in range(1, n + 1):
    print((" " * (n - i)) + ("*" * i))