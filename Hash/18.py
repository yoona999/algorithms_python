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
