c_score = 100
s_score = 100

for _ in range(int(input())):
    c, s = map(int, input().split())

    if c > s :
        s_score -= c

    elif s > c:
        c_score -= s

    else:
        continue

print(c_score)
print(s_score)

# print(f"{c_score}\n{s_score}")