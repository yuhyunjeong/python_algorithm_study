t = int(input())

score_y = score_k = 0
for _ in range(t):
    for i in range(9) :
        y,k = map(int, input().split())
        
        score_y += y
        score_k += k

    if score_y > score_k :
        print("Yonsei")
    elif score_y < score_k :
        print("Korea")
    else :
        print("Draw")
    