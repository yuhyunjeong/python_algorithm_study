n = int(input())

m = int(input())

result = m

for _ in range(n):
    i, o = map(int, input().split())
    
    m = m + i - o

    if m < 0:
        result = 0
        break
    if result < m:
        result = m

print(result)

# 풀이 2
n = int(input())
m = [int(input())]
for i in range(n):
    I, O = map(int, input().split())
    s = m[i] + I - O
    if s < 0:
        print(0)
        exit()
    else:
        m.append(s)
print(max(m))