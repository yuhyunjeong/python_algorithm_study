import itertools

def solution(number):
    # 학생 세명의 정수 번호를 더했을때 0이 되는 방법의 수
    answer = 0

    for i in list(itertools.combinations(number, 3)): #세개씩 묶은 조합 (1,2,3)
        if sum(i) == 0 : # 조합의 합이 0이라면
            answer += 1
    return answer






# 브루트포스
def solution(number):
    answer = 0
    n = len(number)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer


#투포인터
def solution(number: list) -> list:
    results = []
    number.sort()
    answer = 0

    for i in range(len(number) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and number[i] == number[i - 1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(number) - 1
        while left < right:
            sum = number[i] + number[left] + number[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:# sum = 0인 경우이므로 정답 및 스킵 처리
                results.append([number[i], number[left], number[right]])
                while left < right and number[left] == number[left + 1]:
                    left += 1
                while left < right and number[right] == number[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    
    answer = len(results)

    return answer