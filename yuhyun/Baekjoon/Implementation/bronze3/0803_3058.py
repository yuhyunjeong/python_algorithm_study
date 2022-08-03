T = int(input())
for _ in range(T):
    num = list(map(int, input().split())) 

    result=[]

    for i in num:
        if i % 2 == 0 :
            result.append(i)

    # num = [i for i in list(map(int, sys.stdin.readline().split())) if i % 2 == 0]

    result.sort()

    print(sum(result), result[0])