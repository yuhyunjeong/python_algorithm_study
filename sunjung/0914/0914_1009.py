from sys import stdin

t = int(input())
for _ in range (t) :
    a,b = map(int, stdin.readline().split())
    # 마지막 데이터가 처리될 컴퓨터의 번호
    # x**y = x의 y승
    print((a**b)%10)

#다음 풀이
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10
    
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a**4) % 10 % 10 % 10)
        else:
            print((a**b) % 10 % 10 % 10)