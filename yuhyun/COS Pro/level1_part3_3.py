def solution(K, words):
    answer = 1
    i = len(words[0])
    for word in words[1:]:
        if i + len(word) + 1 <= K:
            i += len(word) + 1
        else:
            answer += 1
            i = len(word)
    return answer