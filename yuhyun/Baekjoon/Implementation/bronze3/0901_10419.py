for i in range(int(input())):
    d = int(input())
    t = 0
    
    while 1:
        if t + t**2 <= d:
            result = t
            t+=1
        else:
            break
    print(result)
   