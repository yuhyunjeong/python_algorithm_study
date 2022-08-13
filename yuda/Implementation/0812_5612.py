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