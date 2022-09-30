# 낮은 숫자가 나온 사람은 상대편 주사위에 나온 숫자만큼 점수를 잃게 된다. 
# 두 사람의 주사위가 같은 숫자가 나온 경우에는 아무도 점수를 잃지 않는다.
score_a = score_b = 100

for _ in range(int(input())) :
    a,b = map(int, input().split())
    if a>b :
        score_b-=a
    if b>a :
        score_a-=b

print(score_a)
print(score_b)
    

