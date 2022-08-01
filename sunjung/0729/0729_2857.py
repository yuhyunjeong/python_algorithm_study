
name = []

for _ in range (5) :
   name.append(input())

yes = 0
for i in range(len(name)) :
    if 'FBI' in name[i] :
        print(i+1, end=' ')
        yes = 1

if yes == 0 :
    print('HE GOT AWAY!')