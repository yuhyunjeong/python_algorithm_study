# 첫째 줄에 공이 들어있는 컵의 번호를 출력한다. 
# 공이 사라져서 컵 밑에 없는 경우에는 -1을 출력한다.

cup = [1,2,3]
for _ in range(int(input())):
    x, y = map(int, input().split())
    
    x = cup.index(x)
    y = cup.index(y)
    cup[x], cup[y] = cup[y], cup[x]
    
print(cup[0])