for _ in range(int(input())):
    n = int(input())
    print(f"Case {_+1}:")
    for a in range(1, 7):  #1~6까지 반복
        for b in range(a, 7): #x~6까지
            if a+b == n:
                print(f"({a},{b})")