import math

def solution(progresses, speeds):
    ans = []
    n = len(progresses)

    left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    max_day = left[0]
    cnt = 0

    for i in range(1, n):
        if left[i] > max_day:
            ans.append(cnt)
            cnt = 1
            max_day = left[i]
        else:
            cnt += 1
    ans.append(cnt)
    return ans  