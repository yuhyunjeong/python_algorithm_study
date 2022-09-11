n = int(input())
nine = ""
while n != 0:
    nine += str(n % 9)
    n //= 9
print(int(nine[::-1]))