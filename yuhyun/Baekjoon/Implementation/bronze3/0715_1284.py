while True:
    N = input()
    width=0

    if N == "0" :
        break

    for i in N :
        if int(i) == 1:
            width+=2
        elif int(i) == 0:
            width+=4
        else:
            width+=3
    print(width+len(N)+1)
    
        
