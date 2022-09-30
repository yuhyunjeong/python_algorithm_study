n,t = map(int, input().split())
a = list(map(int,input().split()))

result = 0 #결과값 초기화 

for i in a :
    t -= i
    if t>=0:
        result +=1
    else:
        break
print(result)

