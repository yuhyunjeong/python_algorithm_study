T = int(input())
jjak = []  

for _ in range(T):
    num = list(map(int, input().split()))

    for i in num : 
        if i % 2 == 0 :
            jjak.append(i)

    print(sum(jjak),min(jjak))