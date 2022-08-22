import sys

while 1:
    try:
        h, p = map(int, input().split()) # try - except : input()
        avg = h / p
    except:
        break

    print('%.2f' %avg)

# 풀이 2

lst = sys.stdin.readlines() # readlines() - list
for i in lst:
    h, p = map(int, i.split())
    avg = h / p
    print('%.2f' %avg)