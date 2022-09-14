vm = {1:500, 2:800, 3:1000}
result = 5000
for i in list(map(int, input().split())):
    result -= vm[i]
print(result)