for a in range(6,101):
    for b in range(2,101):
        for c in range(b+1,101):
            for d in range(c+1,101):
                if a**3 == b**3 + c**3 + d**3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
                if a**3 < b**3 + c**3 + d**3:
                    break

#두번째 풀이
for i in range(6, 101):
    for j in range(2, i):
        for k in range(j, i):
            for l in range(k, i):
                if i ** 3 == j ** 3 + k ** 3 + l ** 3:
                    print("Cube = %d, Triple = (%d,%d,%d)" % (i, j, k, l))

