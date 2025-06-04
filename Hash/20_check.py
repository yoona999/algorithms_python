# 완주하지 못한 선수의 이름을 반환
# dic[key] = 0인 선수는 완주, dic[key] = 1인 선수는 완주하지 못한 것
def solution(participant, completion):
  dic = { }

  for p in participant:
    if p in dic:
      dic[p] += 1
    else:
      dic[p] = 1

  for c in completion:
    dic[c] -= 1

  for key in dic.keys( ) :
    if dic[key] > 0:
      return key