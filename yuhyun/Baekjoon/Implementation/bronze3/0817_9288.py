t = int(input())

for n in range(t):
    num = int(input())

    print(f"Case {n+1}:")

    for i in range(1,7):

        for j in range(i,7):

            if i + j == num:           
                print(f"({i},{j})")

        
            

        
    


