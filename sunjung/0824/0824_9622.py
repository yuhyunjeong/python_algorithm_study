ok = 0
for _ in range(int(input())) :
    len,width,cm,kg = map(float, input().split())
    if (len > 56 or width > 45 or cm > 25) and (len+width+cm) > 125 or kg > 7 :
        print(0)
    else :
        ok += 1
        print(1)

print(ok)
