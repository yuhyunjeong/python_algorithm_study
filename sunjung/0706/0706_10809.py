str = input()
alph = list(range(97,123)) #아스키코드 범위(a= 97,z= 122)

for i in alph :
    print(str.find(chr(i)),end=" ")

    # chr( ) 함수는 숫자(아스키코드) -> 문자로 변환하는 함수