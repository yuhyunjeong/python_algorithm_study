a = b = c = d = 0


for a in range(6,101):
    for b in range(2,a): # 1보다 큰 자연수
        for c in range(b+1,a):
            for d in range(c+1,a):
                    
                if a**3 == b**3 + c**3 + d**3:
                        
                        
                     print(f"Cube = {a}, Triple = ({b},{c},{d})")

                     #풀이 2
                     print("Cube = %d, Triple = (%d,%d,%d)" % (a, b, c, d))
