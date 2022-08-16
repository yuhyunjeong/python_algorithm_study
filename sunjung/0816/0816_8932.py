from sys import stdin

def track(A,B,C,P) :
    return int(A*(B-P)**C)

def field(A,B,C,P) :
    return int(A*(P-B)**C)


for _ in range (int(input())) :
    n = list(map(int, stdin.readline().split()))
    result = track(9.23076, 26.7, 1.835, n[0]) + field(1.84523, 75, 1.348, n[1]) + \
    field(56.0211, 1.5, 1.05, n[2]) + track(4.99087, 42.5, 1.81, n[3]) + \
    field(0.188807, 210, 1.41, n[4]) + field(15.9803, 3.8, 1.04, n[5]) + \
    track(0.11193, 254, 1.88, n[6])
    
    print(result)
