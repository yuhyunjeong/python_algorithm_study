num=[]

for _ in range(9) :
    n = int(input())
    num.append(n)

print(max(num))
print(num.index(max(num))+1)

# 풀이 2
num = [int(input()) for _ in range(9)]
print(max(num))
print(num.index(max(num)) + 1)
