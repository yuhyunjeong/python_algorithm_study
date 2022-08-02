T = int(input())

for _ in range(T):
    
    num, unit = input().split()
    num = float(num)
    
    if unit == "kg":
        num *= 2.2046
        unit="lb"
        
    elif unit == "lb":
        num *= 0.4536
        unit="kg"
        
    elif unit == "l":
        num *= 0.2642
        unit="g"
       
    elif unit == "g":
        num *= 3.7854
        unit="l"
        
    print(format(num,".4f"), unit) # 반올림 후 소수점 특정 자리수까지 출력

# 풀이 2
import sys

W = {"kg":2.2046, "lb":0.4536, 'l':0.2642, 'g':3.7854}
D = {"kg":"lb", "lb":"kg", 'l':"g", 'g':"l"}

for _ in range(int(sys.stdin.readline())):
    N = sys.stdin.readline().split()

    weight = float(N[0]) * W.get(N[1])
    danwi = D.get(N[1])

    print("%.4f" % weight, danwi)


