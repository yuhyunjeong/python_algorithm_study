# R(바위) S(가위), P(보)
# R > S , R < P, S > P

for i in range(int(input())) :
    p1 = p2 = 0 
    for j in range(int(input())) :
        a, b = input().split()
        if a=='R' and b=='S': #바위>가위
            p1 += 1
        elif a=='R' and b=='P': #바위<보
            p2 += 1
        elif a=='S' and b=='R': #가위<바위
            p2 += 1
        elif a=='S' and b=='P': #가위>보
            p1 += 1
        elif a=='P' and b=='S': #보<가위
            p2 += 1
        elif a=='P' and b=='R': #보>바위
            p1 += 1
        else :
            continue

    if p1> p2 :
        print('Player 1')
    elif p1< p2 :
        print('Player 2')
    else :
        print('TIE')
