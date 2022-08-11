T = int(input())

for _ in range(T):
    n = int(input())

    if n == 1 or n == 2:
        for i in range(n):
            print("#"*n)
    else:
        print("#"*n)
            
        for j in range(n-2):
            print("#",end='')            
            print("J"*(n-2),end='')
            print("#")
            
        print("#"*n)
        
    print()

# 풀이 2
for i in range(int(input())):
    n = int(input())
    for i in range(n):
        if i == 0 or i == n - 1:
            print("#" * n)
        else:
            print("#" + "J" * (n - 2) + "#")
    print()
        
        
