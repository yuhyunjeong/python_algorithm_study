snack = ["S", "N", "U"]
s = [list(map(int, input().split())) for _ in range(len(snack))]
for i in range(len(s)):
    s[i][0] = s[i][0] * 10 if s[i][0] * 10 < 5000 else s[i][0] * 10 - 500
    s[i][1] *= 10
    s[i] = s[i][1] / s[i][0]
print(snack[s.index(max(s))])