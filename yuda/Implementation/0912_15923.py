q = int(input())
dot = [list(map(int, input().split())) for _ in range(q)]
count = abs(dot[0][0] - dot[-1][0]) + abs(dot[0][1] - dot[-1][1])
for i in range(q - 1):
    count += abs(dot[i][0] - dot[i + 1][0]) + abs(dot[i][1] - dot[i + 1][1])
print(count)