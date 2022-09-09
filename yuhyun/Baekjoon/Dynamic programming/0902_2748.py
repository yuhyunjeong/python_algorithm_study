n = int(input())
num = []
result = 0

for i in range(n+1):

    if i == 0:
        result = 0
        
    elif i == 1:
        result = 1
        
    else:
        result = num[i-1] + num[i-2]
    
    num.append(result)

print(num[n])

