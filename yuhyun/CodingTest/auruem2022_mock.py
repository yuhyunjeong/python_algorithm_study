# 1. 3개의 좌표가 주어질 때 직사각형 만들기 위한 1개의 좌표 찾기

def solution(v):
    answer = []

    x_dot = []
    y_dot = []

    for i in range(3):
 
        x_dot.append(v[i][0])
        y_dot.append(v[i][1])

   
    x_result = 0
    y_result = 0

    for i in range(3):
    
        if x_dot.count(x_dot[i]) == 1:
            x_result = x_dot[i]

        if y_dot.count(y_dot[i]) == 1:
            y_result = y_dot[i]
    
    answer = [x_result, y_result]

    return answer

# 2. 별찍기

n = int(input().strip())
for i in range(n):
    print('*'*(i+1))

# 3. 1 ~ n 까지 배열에 담기

def solution(n):
    answer = []
    for i in range(n):
        answer.append(i+1)
    return answer

# 4.
# SELECT BRANCH_ID , SUM(SALARY) AS TOTAL FROM EMPLOYEES GROUP BY BRANCH_ID ORDER BY BRANCH_ID

# 5.
# (1) TCP 통신과 UDP 통신의 차이점:
# TCP : 연결형 서비스 , 전송 순서 보장, 수신 여부 확인, 신뢰성 높음, 속도 느리다
# UDP : 비연결형 서비스, 전송 순서가 바뀔 수 있음, 수신 여부를 확인하지 않음, 신뢰성 낮음, 속도 빠르다 

# (2) TCP 통신을 사용하는 곳:
# HTTP 통신, 이메일이나 파일전송처럼 순서대로 도착해야 하는 상황에서 사용된다.

# (3) UDP 통신을 사용하는 곳:
# 순서는 보장해주지 못하지만 실시간으로 반응해야하는 실시간 동영상 플레이어나 게임, 혹은 DNS에서 사용된다.

