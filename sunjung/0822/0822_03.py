def solution(n, roads, sources, destination):
    #n - 총 지역의 수 
    #roads- 두 지역을 왕복, 길 정보 2차원 정수 배열
    #sources- 각 부대원이 위치한 서로 다른 지역 정수 배열
    #destination - 강철부대의 지역

    #강철부대로 복귀할 수 있는 최단시간을 담은 배열 구하기
    #복귀 불가능한 경우 최단 시간은 -1
    #두 지역간의 길을 통과하는데 걸리는 시간은 모두 1로 동일

    answer = []
    return answer