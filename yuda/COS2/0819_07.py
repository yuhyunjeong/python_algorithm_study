def solution(s):
    s_lst = list(s)
    n = len(s)
    for i in range(n):
        # 단순 if문 두 개이기 때문에 z로 바뀐 것도 a로 다시 바꿈
        # 때문에 if를 elif로 변경
        if s_lst[i] == 'a':
            s_lst[i] = 'z'
        elif s_lst[i] == 'z':
            s_lst[i] =  'a'
    return "".join(s_lst)