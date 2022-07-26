H, M = map(int, input().split())

if M < 45 :
    
    if H ==0 :
        print(23, 15+M)
    else :
        print(H-1, 60-(45-M))
else :
    print(H, M-45)

# 풀이 2 
time = list(map(int, input().split()))

time[0] += (time[1] - 45) // 60
time[1] = (time[1] - 45) % 60
if time[0] < 0:
    time[0] += 24

print(*time)