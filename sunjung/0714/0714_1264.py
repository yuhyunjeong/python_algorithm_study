m = ['a','e','i','o','u']

while True:
    cnt = 0
    s = list(input().lower())  # 문자열을 리스트로 입력, 소문자로 변경
    if s[0] == '#': # '#'을 첫 글자로 입력받으면 종료
        break
    # s의 문자열에 모음이 있을 경우 cnt 1씩 추가
    for i in s:
        if i in m:
            cnt += 1
    print(cnt)