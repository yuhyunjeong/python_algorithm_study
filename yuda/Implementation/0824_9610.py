N = int(input())
Q = [0] * 5
for _ in range(N):
    x, y = map(int, input().split())
    if x * y == 0:
        Q[4] += 1
    elif x > 0 and y > 0:
        Q[0] += 1
    elif x < 0 and y > 0:
        Q[1] += 1
    elif x < 0:
        Q[2] += 1
    else:
        Q[3] += 1
for i in range(4):
    print(f"Q{i + 1}: {Q[i]}")
print(f"AXIS: {Q[4]}")