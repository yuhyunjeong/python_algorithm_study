import math
import sys;

# map(function,iterable)
A,B = map(int,sys.stdin.readline().split());

print(A+B)
print(A-B)
print(A*B)

print(math.trunc(A/B))
print(int(A/B))
print(A//B)

print(A%B)