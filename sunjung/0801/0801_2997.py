num = list(map(int,input().split(' ')))
num.sort() #오름차순으로 정렬 4 6 8 / 1 4 10

if num[1] - num[0] == num[2] - num[1] :
    print(num[2]+(num[2]-num[1]))

elif num[2] - num[1] > num[1] - num[0] :
    print(num[1]+(num[1] - num[0]))
    
elif num[2] - num[1] < num[1] - num[0] :
    print(num[0]+(num[2] - num[1]))
