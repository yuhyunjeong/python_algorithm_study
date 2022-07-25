people = []
x = 0

for _ in range (10) :
    a, b = map(int, input().split()) #a=내린사람 b=탄사람
    x += b #탄사람
    x -= a #내린사람

    people.append(x) #리스트에 추가

print(max(people))