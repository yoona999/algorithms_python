# 회원가입시 정현이가 원하는 제품을 모두 할인받을 수 있는 회원 등록 날짜의 총 일수 반환

# dictonary로 표현할 것: 
# 1. 내가 사려고 하는 제품과 제품의 개수
# 2. n일 차에 회원가입을 하면 할인받아 살 수 있는 제품과 제품의 개수
# ==을 사용해 dictonary가 완전히 일치하는지 확인 가능

def solution(want, number, discount):

  # 1.
  want_dict = { } # 구매하려는 제품
  for i in range(len(want)):
    want_dict[want[i]] = number[i]

  answer = 0 

  # 2.
  for i in range(len(discount) - 9):
    discount_10d = { } # i일 회원가입시 할인받는 제품 및 개수

    # i일 회원가입 시 할인받는 제품 및 개수
    for j in range(i, i + 10):
      if discount[j] in want_dict:
        discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1

    # i일 회원가입시 할인받는 제품 및 개수가 내가 사려고 하는 제품과 일치하는지 확인
    # i일에 구매하려는 모든 제품을 할인받는다면 answer 증가하게끔
    if discount_10d == want_dict:
      answer += 1

  return answer