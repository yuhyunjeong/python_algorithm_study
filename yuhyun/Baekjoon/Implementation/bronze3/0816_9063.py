N = int(input())

x_lst = []
y_lst = []

for i in range(N):
    x, y = map(int, input().split())

    x_lst.append(x)
    y_lst.append(y)

x_result = max(x_lst)-min(x_lst)
y_result = max(y_lst)-min(y_lst)

print(x_result*y_result)
