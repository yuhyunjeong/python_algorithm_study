result = []
for _ in range(3) :
    result = list(map(int, input().split()))
    # 0=1 -A(도) , 0=2-B(개) , 0=3-C(걸), 0=4-D(윷), 0=5-E(모)

    if result.count(0) == 1 :
        print('A')
    elif result.count(0) == 2:
        print("B")
    elif result.count(0) == 3:
        print("C")   
    elif result.count(0) == 4:
        print("D")
    else:
        print("E") 