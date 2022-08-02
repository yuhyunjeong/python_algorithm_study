num = input()

if num == "1 2 3 4 5 6 7 8" :
    print("ascending")
elif num == "8 7 6 5 4 3 2 1" :
    print("descending")
else :
    print("mixed")

# 풀이 2
num = list(map(int, input().split()))

if num == sorted(num) :
    print('ascending')
elif num == sorted(num, reverse=True):
    print('descending')
else:
    print('mixed')