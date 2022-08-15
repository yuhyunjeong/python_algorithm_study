# 풀이 1
while True:
    try:
        H, P = map(int, input().split())
    except:
        break
    print("%.2f" % (H / P))

# 풀이 2
import sys
lst = sys.stdin.readlines()
for i in lst:
    H, P = map(int, i.split())
    print("%.2f" % (H / P))