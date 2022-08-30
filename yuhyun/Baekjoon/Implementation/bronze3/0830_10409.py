n, t = map(int, input().split())
num = list(map(int, input().split()))
result = 0
cnt = 0

for i in num:
    
    result += i

    if result > t:
        break
    
    cnt += 1

print(cnt)
