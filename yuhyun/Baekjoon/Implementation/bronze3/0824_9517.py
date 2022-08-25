K = int(input())
time = 0
result = 0

for _ in range(int(input())):
    T, Z = input().split()

    time += int(T)

    if time >= 210:
        print(K)
        break

    if Z == "T":
        K += 1
        if K == 9:
            K = 1
    elif Z == "N" or Z == "P":
        continue

