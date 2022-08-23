for _ in range (int(input())) :
    n,d = map(int, input().split()) #우주선 개수, 목적지까지의 거리

    num = 0
    for i in range (n) :
        v,f,c = map(int, input().split()) #우주선의 최고속도, 연료 양, 연료 소비율
        if v * (f / c) >= d: # 최고속도 * (연료양/연료소비율) >= 목적지까지의 거리
            num += 1
    print(num)