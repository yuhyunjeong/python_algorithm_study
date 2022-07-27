import sys

W = {"kg":2.2046, "lb":0.4536, 'l':0.2642, 'g':3.7854}
D = {"kg":"lb", "lb":"kg", 'l':"g", 'g':"l"}

for _ in range(int(sys.stdin.readline())):
    N = sys.stdin.readline().split()

    weight = float(N[0]) * W.get(N[1])
    danwi = D.get(N[1])

    print("%.4f" % weight, danwi)