# numbers에서 서로 다른 인덱스에 있는 두개의 수를 뽑아 더해 만들 수 있는 모든 수를 배열에
# 오름차순으로 담아 반환

# .sort()한 후 return/print 하는 경우 -> OK
def solution(numbers):
    ans = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            ans.append(numbers[i]+numbers[j])
    ans.sort(reverse = False) # ans 리스트 자체를 변경시킴
    return list(set(ans))

print(solution([2,1,3,4,1]))

# 또는
# sorted method를 사용하는 경우 -> OK
def solution(numbers):
    ans = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            ans.append(numbers[i]+numbers[j])
    return sorted(set(ans))

print(solution([2,1,3,4,1]))