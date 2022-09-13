# python3 - 78점 / pypy3 - 100점

n  = input()

cnt = 0

for i in range(1, int(n)+1):

    num = 0

    for j in str(i):
        num += int(j)

    if i % num == 0:
        cnt += 1

print(cnt) 