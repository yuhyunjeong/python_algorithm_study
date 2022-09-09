cup = [1, 0, 0, 2]
C = input()
for c in C:
    if c == 'A':
        cup[0], cup[1] == cup[1], cup[0]
    elif c == 'B':
        cup[0], cup[2] == cup[2], cup[0]
    elif c == 'C':
        cup[0], cup[3] == cup[3], cup[0]
    elif c == 'D':
        cup[1], cup[2] == cup[2], cup[1]
    elif c == 'E':
        cup[1], cup[3] == cup[3], cup[1]
    else:
        cup[2], cup[3] == cup[3], cup[2]
print(cup.index(1) + 1)
print(cup.index(2) + 1)