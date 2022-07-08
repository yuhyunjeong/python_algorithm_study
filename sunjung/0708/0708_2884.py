# 알람시계

h, m = map(int, input().split())

if m >= 45 :	
    print(h, m-45) #현재 -45분

elif h> 0 and m <45 : #현재시간 45분보다 작다(빠름) - 한시간 빼고, 15분 더한다
    print(h-1, m+15)

else :                #현재시간 0시일때, 45분보다 작다(빠름) - 시간 23시, +15분
    print(23, m+15) 

#풀이2

if m < 45 :
    if h ==0:
        print()

#풀이3
time = list(map(int, input().split()))

time[0] += (time[1] - 45) // 60
time[1] += (time[1] - 45) % 60

if time[0] < 0 :
    time[0] += 24

print(*time)
