A, B = input().split()

A = int(A[::-1]) # step
B = int(B[::-1])

print(max(A,B))