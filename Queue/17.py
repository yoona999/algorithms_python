from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal: # goal이랑 일치하면 popleft
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else: # goal의 첫 번째 원소가 cards1이나 cards2의 첫 번째 원소와 일치하지 않으면
            return "No"
        
    return "Yes"