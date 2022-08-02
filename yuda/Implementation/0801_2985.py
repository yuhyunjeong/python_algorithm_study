A, B, C = map(int, input().split())
if A + B == C:
    F = "+"
    S = "="
elif A == B + C:
    F = "="
    S = "+"
elif A == B - C:
    F = "="
    S = "-"
elif A * B == C:
    F = "*"
    S = "="
elif A == B * C:
    F = "="
    S = "*"
else:
    F = "="
    S = "/"
print(A, F, B, S, C, sep="")