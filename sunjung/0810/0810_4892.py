i = 1
while True:
    n0 = int(input())
    if(n0==0) :
        break
    n1 = 3*n0

    if n1%2==0 : #짝수라면
        n2 = n1/2
        print(f"{i}. even", end=' ')

    elif n1%2!=0 : #홀수라면
        n2 = (n1+1)/2
        print(f"{i}. odd", end=' ')

    n3 = 3*n2
    n4 = n3//9 # n4는 나눗셈의 몫
    print(int(n4))
    i += 1




#다른 풀이
""" i = 1
while True:
    n = int(input())
    if not n:
        break
    print(f"{i}. odd {n // 2}" if n % 2 else f"{i}. even {n // 2}")
    i += 1 """





""" i = 1
while 1:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3*n0
    n2 = (n1+1)//2 if n1%2 else n1//2
    n3 = 3*n2
    n4 = n3//9
    if n0 == 2*n4:
        print(f"{i}. even {n4}")
    else:
        print(f"{i}. odd {n4}")
    i += 1 """