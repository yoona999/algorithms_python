def solution(lst):
    uniq_lst = list(set(lst)) # O(N)
    uniq_lst.sort(reverse=True) # O(NlogN)
    return uniq_lst

# 최종 O(NlogN)

print(solution([1, -3, 2, 4, 3]))