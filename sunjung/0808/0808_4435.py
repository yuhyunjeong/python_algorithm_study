for i in range (int(input())) :
    gandalf = list(map(int, input().split())) #간달프
    sauron = list(map(int, input().split())) #사우론

    g_score = gandalf[0] + gandalf[1]*2 + gandalf[2]*3 + gandalf[3]*3 + gandalf[4]*4 + gandalf[5]*10
    s_score = sauron[0] + sauron[1]*2 + sauron[2]*2 + sauron[3]*2 + sauron[4]*3 + sauron[5]*5 + sauron[6]*10

    if g_score > s_score :
        print(f'Battle {i+1}: Good triumphs over Evil') 
    elif g_score < s_score :
        print(f'Battle {i+1}: Evil eradicates all trace of Good') 
    else :
        print(f'Battle {i+1}: No victor on this battle field') 
    








