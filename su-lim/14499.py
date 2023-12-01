import sys
input = sys.stdin.readline

# init
N, M, y, x, K = map(int, input().split())
maps = []
for _ in range(N):
  maps.append(list(map(int, input().split())))
command = list(map(int, input().split()))

dxdy = [(0,0), (1,0), (-1,0), (0,-1), (0,1)]
dices = [0,0,0,0,0,0]
result = []

def roll(direct, dices):
  tmp_dices = dices.copy()
  if direct == 1: #동
    tmp_dices[2] = dices[0]
    tmp_dices[5] = dices[2]
    tmp_dices[0] = dices[3]
    tmp_dices[3] = dices[5]
  if direct == 2: #서
    tmp_dices[3] = dices[0]
    tmp_dices[0] = dices[2]
    tmp_dices[5] = dices[3]
    tmp_dices[2] = dices[5]
  if direct == 3: #북
    tmp_dices[1] = dices[0]
    tmp_dices[5] = dices[1]
    tmp_dices[0] = dices[4]
    tmp_dices[4] = dices[5]
  if direct == 4: #남
    tmp_dices[4] = dices[0]
    tmp_dices[0] = dices[1]
    tmp_dices[5] = dices[4]
    tmp_dices[1] = dices[5]
  return tmp_dices


# main
for com in command:

  # 1. 이동할 수 있나?
  dx, dy  = dxdy[com]
  if x+dx < 0 or y+dy < 0 or x+dx >= M or y+dy >= N:
    continue
  x += dx
  y += dy

  # 2. 이동 후 주사위 결과 / roll
  dices = roll(com, dices)

  # 3. 윗면 출력
  print(dices[0])

  # 4. 바닥면 업데이트
  if maps[y][x] == 0:
    maps[y][x] = dices[-1]
  else:
    dices[-1] = maps[y][x]
    maps[y][x] = 0