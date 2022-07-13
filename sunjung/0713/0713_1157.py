
word = input().upper()
alph = list(set(word)) #단어 중복제거 후 리스트에 담기
re= []

for i in alph:
    count = word.count(i) #처음 입력받은 변수에서 문자 갯수 세기
    re.append(count)

if re.count(max(re)) >=2: #배열에서 최댓값이 두가지 이상이라면
    print("?")

else:
    print(alph[re.index(max(re))].upper())



