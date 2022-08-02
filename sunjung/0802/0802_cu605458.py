#6054
a, b = map(int, input().split())

if (bool(a) and bool(b) == True):
    print("True")
else:
    print("False")

#6055
a, b = map(int, input().split())

if (bool(a) or bool(b) == True):
    print("True")
else:
    print("False")

#6056
# XOR 연산자(^)는 bool값이 서로 같으면 False, bool값이 서로 다르면 True 를 출력
a, b = map(int, input().split())

if (bool(a) ^ bool(b) == True): #값이 서로 다를때
    print("True")
else:
    print("False")

#6057
a, b = map(int, input().split())

if (bool(a) ^ bool(b) == True): #값이 서로 다를때
    print("False")
else:
    print("True")

#6058
a, b = map(int, input().split())
a, b = bool(a), bool(b)

if (a == False and b == False):
    print("True")
else:
    print("False")

