x,y = map(int, input().split())
n = int(input())

price = [(x/y)*1000]
a = 0

for i in range(n) :
    xi,yi = map(int, input().split())
    a = (xi/yi)*1000
    price.append(a)

print(round(min(price),2))