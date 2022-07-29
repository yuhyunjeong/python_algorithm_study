fbi = []

for i in range(5):
    name = input()
    if "FBI" in name:
        fbi.append(i + 1)

if len(fbi) == 0:
    print("HE GOT AWAY!")
else:
    print(*fbi)