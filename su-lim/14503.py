# d : 0 북 1 동 2 남 3 서
# 0 청소안된 빈칸, 1 벽 칸, 2 청소한 칸

# input
N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
result = 0
d_set = [(-1,0),(0,1),(1,0),(0,-1)] # 북 동 남 서

while True:

  # 1. 현재 칸이 청소되지 않은 경우 - 현재칸 청소
  if maps[r][c] == 0:
    maps[r][c] = 2
    result += 1

  check = 0

  # 2. 현재 칸의 주변 4칸 중
  for dx, dy in d_set:

    if r+dx < 0 or r+dx >= N or c+dy < 0 or c+dy >= M:
      continue

    # 2-1. 빈칸 있는 경우
    if maps[r+dx][c+dy] == 0:
      check = 1

      # 반시계 회전
      d = (d+3)%4

      # 가능한 범위이면서
      if 0 <= r+d_set[d][0] < N and 0 <= c+d_set[d][1] < M:
        # 해당 방향에서 앞칸이 청소되지 않은 빈칸인 경우 한칸 전진
        if maps[r+d_set[d][0]][c+d_set[d][1]] == 0:
          r, c = r+d_set[d][0], c+d_set[d][1]
      break

  # 2-2.빈칸이 없는 경우
  if check == 0:
  # 2-2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면, 한 칸 후진하고 1번으로 돌아감
    new_d = (d+2)%4
    # 후진 가능한 범위이면서, 벽이 없으면 처음으로
    if 0 <= r+d_set[new_d][0] < N and 0 <= c+d_set[new_d][1] < M:
      if maps[r+d_set[new_d][0]][c+d_set[new_d][1]] != 1:
        r, c = r+d_set[new_d][0], c+d_set[new_d][1]
        continue
    # 2-1-2. 후진 불가 시 END
    break

print(result)