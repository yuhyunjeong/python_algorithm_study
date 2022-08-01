a,b = map(int, input().split())
c,d = map(int, input().split())
list = [a/c+b/d,    #0번
        c/d+a/b,    #1번
        d/b+c/a,    #2번
        b/a+d/c]    #3번
print(list.index(max(list))) #최대값이 들어있는 인덱스 출력
