import sys
#kg(킬로그램), lb(파운드), l(리터), g(갤런)
T = int(input()) #테스트 케이스의 수
for _ in range(T) :
    x,y = input().split() #x=값, y=단위
    if y=='kg':print("%.4f lb" % (float(x)*2.2046)) #%.4f = 소수점 4째자리까지
    elif y == 'l': print("%.4f g" % (float(x) * 0.2642))
    elif y == 'lb': print("%.4f kg" % (float(x) * 0.4536))
    elif y == 'g': print("%.4f l" % (float(x) * 3.7854))