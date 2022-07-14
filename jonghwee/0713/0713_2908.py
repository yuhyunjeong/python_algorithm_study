import sys

L2 = [];
L = list(sys.stdin.readline().split());
for i in L:
    L2.append(int(i[::-1])) #이거 int로 안바꿔도 정답 처리됨

print(max(L2))