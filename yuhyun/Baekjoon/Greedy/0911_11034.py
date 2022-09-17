while True:

    # 무한 입력일때 오류가 난다면 try - except

    try:
        a, b, c = map(int, input().split())
        print(max(b - a , c - b)-1) # 최대로 움직이는 경우
    except:
        break
