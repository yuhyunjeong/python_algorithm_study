x = list(map(int, input().split()))
y = list(map(int, input().split()))
result = "Y"

for i in range (5):
    if x[i]==y[i] :
        result = "N"
        break


print(result)

