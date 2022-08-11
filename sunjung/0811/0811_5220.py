
gum_bit = 0
for _ in range (int(input())) :
    a,b = map(int, input().split())
    a = str(format(a, 'b')) #a를 이진수로 바꾸고 string으로 변환

    if (a.count('1'))%2 ==0 : #짝수
        gum_bit = 0
    else :
        gum_bit = 1

    if b == gum_bit :
        print('Valid')
    else :
        print('Corrupt')

