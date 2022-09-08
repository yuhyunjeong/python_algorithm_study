# 풀이 1
A = list(map(int, input().split()))
B = list(map(int, input().split()))
while A[1] > 0 or B[1] > 0:
    A[1] -= B[0]
    B[1] -= A[0]
if A[1] == B[1]:
    print("DRAW")
elif A[1] > B[1]:
    print("PLAYER A")
else:
    print("PLAYER B")
    
# 풀이 2
A = list(map(int, input().split()))
B = list(map(int, input().split()))
while True:
    A[1] -= B[0]
    B[1] -= A[0]
    if A[1] <= 0 and B[1] <= 0:
        print("DRAW")
        break
    elif B[1] <= 0:
        print("PLAYER A")
        break
    elif A[1] <= 0:
        print("PLAYER B")
        break
    
# 풀이 3
import math

A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = math.ceil(A[1] / B[0])
b = math.ceil(B[1] / A[0])
if a == b:
    print("DRAW")
elif a > b:
    print("PLAYER A")
else:
    print("PLAYER B")