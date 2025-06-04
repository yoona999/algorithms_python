# 두 개의 수로 특정값 만들기
# 합이 target인 두 수가 arr에 존재하는지 찾고, 있으면 True, 없으면 False 반환
def count_sort(arr,k):
    hash = [0] * (k + 1)  # k는 최대값
    for num in arr:
        if num <= k:
            hash[num] = 1
    return hash

def solution(arr, target):
    hash = count_sort(arr, target)

    for num in arr:
        complement = target - num
        if(complement != num and complement >= 0 and complement <= target and hash[complement] == 1):
            return True
    return False
