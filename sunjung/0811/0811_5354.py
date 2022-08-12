for _ in range (int(input())) :
    n = int(input())

    if n >= 3: #3보다 같거나 크면 
        print('#' * n) #n만큼 #출력
        for i in range(n - 2): #첫줄 마지막줄 제외하고
            print('#' + 'J' * (n - 2) + '#') #나머지 줄은 양 옆 #두개 제외한 부분에 J를 출력!
        print('#' * n + '\n')

    else: #그 이외에는
        for i in range(n):
            print('#' * n) #n만 출력
        print()


#풀이2
for i in range(int(input())):
    n = int(input())
    for i in range(n):
        if i == 0 or i == n - 1:
            print("#" * n)
        else:
            print("#" + "J" * (n - 2) + "#")
    print()