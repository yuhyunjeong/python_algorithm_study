n = int(input())

pair = [0, 0]
cnt = 0

for i in range(1,500):
    
    pair[0] = i

    for j in range(1,500):

        pair[1] = j

        if pair[0]**2 == pair[1]**2 + n:
            cnt += 1
   

print(cnt)
    