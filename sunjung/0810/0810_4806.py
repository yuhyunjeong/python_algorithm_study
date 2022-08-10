result = []
while True :
    try:
        n = input()
        result.append(n)
    except EOFError:
        break
print(len(result))


#print(len([*open(0)]))

#두번째
import sys

print(len(sys.stdin.readlines()))