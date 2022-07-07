N = int(input())
num = input()
result = 0

for i in range(N) :
    result += int(num[i])

print(result)

# 풀이 2
n = input()
print(sum(map(int,input())))