n = int(input())
a = b = c = 0
cnt = 0

for i in range(1, n+1):
    
    if i % 2 == 0:

        a = i

        for j in range(1, n+1-i):

            for k in range(1, j - 2 + 1):
                
                b = k
                c = j

                if a + b + c == n:
                    cnt += 1

print(cnt)