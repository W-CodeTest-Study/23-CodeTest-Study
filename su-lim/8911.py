# 백준 - 거북이

import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())
controls = []
for _ in range(N):
  controls.append(input())


# 메인 알고리즘
for control in controls:
  direct = 0 # 0 북 1 동 2 남 3 서
  x, y = 0,0 # 현재 위치 지정
  all_x, all_y = [0], [0] # 지나간 x, y 값 저장

  for i in range(len(control)):

    if control[i] == "F":
      if direct == 0:
        y += 1
      if direct == 1:
        x += 1
      if direct == 2:
        y -= 1
      if direct == 3:
        x -= 1

    if control[i] == "B":
      if direct == 0:
        y -= 1
      if direct == 1:
        x -= 1
      if direct == 2:
        y += 1
      if direct == 3:
        x += 1

    # 방향 변경
    if control[i] == "R":
      direct = (direct + 1) % 4
    if control[i] == "L":
      direct = (direct + 4 - 1) % 4

    all_x.append(x)
    all_y.append(y)

  # 종료 후 가장 왼쪽 위, 오른쪽 아래인 좌표의 거리 구함
  w = abs(max(all_x)) + abs(min(all_x))
  h = abs(max(all_y)) + abs(min(all_y))
  print(h*w) # 결과 출력