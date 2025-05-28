def solution(numbers):
    lst = []
    for i in range(len(numbers)-1):
        for j in range(i + 1, len(numbers)):
            lst.append(numbers[i] + numbers[j]) # O(N^2)
    uniq_lst = list(set(lst))  # O(N)
    uniq_lst.sort()  # O(N^2log(N^2))
    return uniq_lst

print(solution([2,1,3,4,1]))