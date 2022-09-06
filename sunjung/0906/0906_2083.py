# 나이가 17세보다 많거나, 몸무게가 80kg 이상이면 성인부

while True :
    name, age, weight = input().split()
    age = int(age)
    weight = int(weight)
    if name =='#' and age==0 and weight==0 :
        break
    if(age > 17) or (weight >= 80) :
        print(f'{name} Senior')
    else :
        print(f'{name} Junior')





