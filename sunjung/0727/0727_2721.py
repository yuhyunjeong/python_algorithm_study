
T = int(input()) #테스트 케이스의 수
for _ in range(T) :
    n = int(input())

    sum = 0
    t = 0

    for i in range(1, n+1):
        for j in range(1,i+2):
            t += j #삼각수의 합
        sum += i * t
        t = 0
    print(sum)


""" 
T(1) = 1
T(3) = 1+2+3

W(3) = 1*T(2) + 2*T(3) + 3*T(4)
       = 1*(1+2) + 2*(1+2+3) + 3*(1+2+3+4)
       = 1*3  + 2*6 + 3*10
       = 4 + 12 + 30 

"""
