while True:
    a, b, c = map(float, input().split()) #속도 무게 강도
    if a==0 and b==0 and c==0: 
        break
    list=[]
    if a<=4.5 and b>= 150 and c>=200:
        list.append("Wide Receiver")

    if a<=6.0 and b>= 300 and c>=500:
        list.append("Lineman")

    if a<=5.0 and b>= 200 and c>=300:
        list.append("Quarterback")

    if len(list)==0 :
         list.append("No positions")

    print(*list)


#풀이2
P = {"Wide Receiver":[4.5, 150, 200], "Lineman":[6.0, 300, 500], "Quarterback":[5.0, 200, 300]}

while True:
    N = list(map(float, input().split()))
    if sum(N) == 0:
        break
    
    position = list(P.keys())
    for k in P.keys():
        for i in range(len(P[k])):
            if i == 0:
                if N[i] > P[k][i]:
                    position.remove(k)
                continue
            if N[i] < P[k][i]:
                position.remove(k)
                break

print(*position) if len(position) else print("No positions")