x_dot = []
y_dot = []

for _ in range(3):
    x, y = map(int,input().split())
    
    x_dot.append(x)
    y_dot.append(y)

x_result = 0
y_result = 0
for i in range(3):
    
    if x_dot.count(x_dot[i]) == 1:
        x_result = x_dot[i]

    if y_dot.count(y_dot[i]) == 1:
        y_result = y_dot[i]

print(x_result,y_result)

# 풀이 2
X = []
Y = []
for _ in range(3):
    x, y = map(int, input().split())
    X.remove(x) if x in X else X.append(x)
    Y.remove(y) if y in Y else Y.append(y)
print(X[0], Y[0])


    


