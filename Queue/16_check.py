import math

# 시간 복잡도 O(n)
def solution(progresses, speeds):
    ans = []
    n = len(progresses)
    # 각 작업이 완료되는 데 필요한 일수를 계산
    left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    max_day = left[0] # 첫 번째 작업의 완료 일수(기준 배포일)
    cnt = 0 # 배포될 작업의 수 카운트

    for i in range(1, n):
        if left[i] > max_day: # 배포 가능일이 가장 늦은 배포일보다 늦으면
            ans.append(cnt)
            cnt = 1
            max_day = left[i]
        else: # 배포 가능일이 가장 늦은 배포일보다 빠르면
            cnt += 1
    ans.append(cnt) # 마지막 카운트된 작업 함께 배포
    return ans  