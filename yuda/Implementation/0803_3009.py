X = []
Y = []
for _ in range(3):
    x, y = map(int, input().split())
    X.remove(x) if x in X else X.append(x)
    Y.remove(y) if y in Y else Y.append(y)
print(X[0], Y[0])