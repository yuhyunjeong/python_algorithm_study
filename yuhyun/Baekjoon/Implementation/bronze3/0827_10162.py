t = int(input())
min = [0,0,0]

while t > 0:
    
    if t >= 300:
        t = t - 300
        min[0]+=1

    elif t < 60:
        t = t - 10
        min[2]+=1

    elif t < 300:
        t = t - 60
        min[1]+=1

if t < 0:
    print(-1)

else:
    print(*min)

#풀이 2
n = int(input())
if n % 10:  # >1
    print(-1)
else:
    print(n // 300, n % 300 // 60, n % 60 // 10)
    