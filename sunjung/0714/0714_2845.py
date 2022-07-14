l, p = map(int, input().split())
cnt = list(map(int, input().split()))
party = l * p
for i in cnt:
    print(i - party, end=' ')