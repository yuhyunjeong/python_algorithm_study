N = int(input())
num = 0
for n in range(1,N+1):
    str = input()

    print(f"String #{n}")

    for i in str:
        
        if i == 'Z':
            print('A',end='')
        else:
            num = int(ord(i))+1        
            print(chr(num),end='')

    print()
    print()

# 풀이 2
for i in range(int(input())):
    result = [chr(i + 1) if i != 90 else 'A' for i in map(ord, input())]
    print(f"String #{i + 1}\n", *result, "\n", sep="")