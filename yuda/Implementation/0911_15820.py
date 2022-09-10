sp, ss = map(int, input().split())
for _ in range(sp):
    t, s = map(int, input().split())
    if t != s:
        print("Wrong Answer")
        exit()
for _ in range(ss):
    t, s = map(int, input().split())
    if t != s:
        print("Why Wrong!!!")
        exit()
print("Accepted")