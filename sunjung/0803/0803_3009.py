
xlist = [] #5 5 7 / 30 10 10 
ylist = [] #5 7 5 / 20 10 20

for _ in range(3) :
    x,y = map(int,input().split(' '))
    xlist.append(x)
    ylist.append(y)

for i in range(3) :
    if xlist.count(xlist[i]) ==1 : #5 5 7
        xx = xlist[i]
        #print(xx) #7

    if ylist.count(ylist[i]) ==1 : #5 7 5
        yy = ylist[i]
        #print(yy) 

print(xx,yy)

#두번째 풀이
X = []
Y = []
for _ in range(3):
    x, y = map(int, input().split())
    X.remove(x) if x in X else X.append(x)
    Y.remove(y) if y in Y else Y.append(y)
print(X[0], Y[0])