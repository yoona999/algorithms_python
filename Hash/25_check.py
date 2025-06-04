# 메뉴 리뉴얼
# 최소 2가지 이상의 단품 메뉴로 구성
# 최소 2명 이상의 손님으로부터 주문된 단품 메뉴 조합에 대해서만 코스 요리 메뉴 후보에 포함

from itertools import combinations # 조합을 구하기 위한 라이브러리
from collections import Counter # 조합의 빈도 쉽게 계산하기 위함

def solution(orders, course):
  answer = [ ]

  for c in course:  
    menu = [ ]
    for order in orders:  
      comb = combinations( # 손님이 주문했던 메뉴에서 n가지를 뽑아 메뉴 조합 구성
        sorted(order), c
      )  
      menu += comb

    counter = Counter(menu)  
    if (len(counter) != 0 and max(counter.values( ) ) != 1): 
      for m, cnt in counter.items( ) :
        if cnt == max(counter.values( ) ): 
          answer.append("".join(m))  

  return sorted(answer) 