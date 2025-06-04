def solution(answers):
    # 1번 수포자: [1, 2, 3, 4, 5]
    first = [1,2,3,4,5]
    # 2번 수포자: [2, 1, 2, 3, 2, 4, 2, 5]
    second = [2,1,2,3,2,4,2,5]
    # 3번 수포자: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    third = [3,3,1,1,2,2,4,4,5,5]

    ans = [0] * 3

    for i in range(len(answers)):
        first_num = i % len(first)
        second_num = i % len(second)
        third_num = i % len(third)

        if first[first_num] == answers[i]:
            ans[0] += 1
        if second[second_num] == answers[i]:
            ans[1] += 1
        if third[third_num] == answers[i]:
            ans[2] += 1
        
    max_score = max(ans)
    result = []
    for i in range(len(ans)):
        if ans[i] == max_score:
            result.append(i + 1)  # 수포자 번호는 1부터 시작하므로 i + 1
    return result

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

# 또는
# 위의 패턴을 각각 나누지 않고 for문으로 한번에 처리
def solution(answers):
    # 수포자들의 패턴
    patterns = [
        [1, 2, 3, 4, 5],          # 1번 수포자
        [2, 1, 2, 3, 2, 4, 2, 5], # 2번 수포자
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번 수포자
    ]

    scores = [0] * 3
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    
    max_score = max(scores)
    highest_scores = [i + 1 for i, score in enumerate(scores) if score == max_score]
    return highest_scores
print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

### 시간 복잡도 O(N)
