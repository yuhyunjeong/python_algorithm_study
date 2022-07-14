while 1 : # 1은 true를 뜻함.
    A, B = map(int, input().split());
    if(A==0 and B==0):
        break;
    else:
        print(A+B);