cf2017 = {1:5000000, 2:3000000, 3:2000000, 4:500000, 5:300000, 6:100000}
cf2018 = {1:5120000, 2:2560000, 3:1280000, 4:640000, 5:320000}
for _ in range(int(input())):
    a, b = map(int, input().split())
    price = 0
    if a <= 21:
        for i in range(1, 7):
            a -= i
            if a <= 0:
                price += cf2017[i]
                break
    
    if b <= 31:
        for i in range(5):
            b -= 2 ** i
            if b <= 0:
                price += cf2018[i + 1]
                break
                
    print(price)