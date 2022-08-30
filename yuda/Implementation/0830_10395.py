A = map(int, input().split())
B = map(int, input().split())
for a, b in zip(A, B):
    if a + b != 1:
        print("N")
        break
else:
    print("Y")