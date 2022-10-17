# s, d, h, c = 13
# joker = 2

n = int(input())

result = 1

for i in range(n):

    result = result * ((15 - i) / (54 - i)) #15 / 54 * 14 / 53 * 13 / 52 ... 

print(result)