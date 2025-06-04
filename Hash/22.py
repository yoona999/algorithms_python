# 오픈 채팅방 모든 기록이 처리된 다음 최종으로 방을 개설한 사람이 보는 메시지를 문자열 배열 형태로
# 반환

def solution(record):
  answer = [ ]
  uid = { }
  for line in record: 
    cmd = line.split(" ") # 각 줄을 하나씩 처리
    if cmd[0] != "Leave":  # Enter, Change인 경우 
      uid[cmd[1]] = cmd[2]
  for line in record:  # 각 줄을 하나씩 처리
    cmd = line.split(" ")

    if cmd[0] == "Enter":
      answer.append("%s님이 들어왔습니다." % uid[cmd[1]])
    elif cmd[0] == "Change":
      pass
    else:
      answer.append("%s님이 나갔습니다." % uid[cmd[1]])
  return answer