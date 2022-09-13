n = int(input())
open = int(input())

if n > 5:
    print("Love is open door")
else:
    for i in range(n - 1):
        print(open if i % 2 else (open + 1) % 2)