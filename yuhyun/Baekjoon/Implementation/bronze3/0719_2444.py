N = int(input())

for i in range(N):
    print(" "*(N-i-1)+"*"*(i+1)+"*"*i)
for i in range(N):
    print(" "*(i+1)+"*"*(N-i+N-i-3))
