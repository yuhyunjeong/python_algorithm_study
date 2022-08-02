import sys


lst = []

for i in range(1,6):
    name = sys.stdin.readline().rstrip()

    if 'FBI' in name:
        lst.append(i)
    
if not lst: # 리스트가 공백이라면 FALSE, 공백이라면 TRUE
    print('HE GOT AWAY!')
else:
    print(*lst) 
