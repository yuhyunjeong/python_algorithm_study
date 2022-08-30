x = list(map(int, input().split()))
y = list(map(int, input().split()))

for i in range(len(x)):
    
    if x[i]+y[i] == 1:
        result = "Y"
    
    if x[i]+y[i] != 1:
        result = "N"
        break

print(result)

