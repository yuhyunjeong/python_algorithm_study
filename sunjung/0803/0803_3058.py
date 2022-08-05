T = int(input())

for _ in range(T):
    num = list(map(int, input().split()))
    jjak = []

    for i in num : 
        if i % 2 == 0 : #나머지가 0인것(짝수)
            jjak.append(i)

    print(sum(jjak),min(jjak))

# num = [i for i in list(map(int, sys.stdin.readline().split())) if i % 2 == 0]