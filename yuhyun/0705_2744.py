word = list(input())

for i in range(len(word)) :
    if word[i].islower()==True : # islower / isupper : bool형태
        word[i] = word[i].upper()
    else :
         word[i] = word[i].lower()
    print(word[i],end="")

# print(input().swapcase()) # 대문자 <-> 소문자