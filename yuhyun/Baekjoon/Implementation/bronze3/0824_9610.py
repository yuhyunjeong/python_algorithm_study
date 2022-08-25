q = [0,0,0,0,0]

for _ in range(int(input())):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        q[0] += 1
    elif x < 0 and y > 0:
        q[1] += 1
    elif x < 0 and y < 0:
        q[2] += 1
    elif x > 0 and y < 0:
        q[3] += 1
    else:
        q[4] += 1

for i in range(4):    
    print(f"Q{i+1}: {q[i]}")
print(f"AXIS: {q[4]}")

