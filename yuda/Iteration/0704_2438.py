while True:
    try:
        n = list(map(int, input().split()))
        print(sum(n))
    except:
        break