# 백준 - 헌내기는 친구가 필요해
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maps = []
input_list = []
start_x = 0

for i in range(N):
  row = input().rstrip()
  tmp = []
  for j in row:
    if j == "I": start_x = i
    tmp.append(j)
  input_list.append(tmp)

start_y = 0
for i in range(M):
  if input_list[start_x][i] == "I":
    start_y = i
    break

queue = deque([[start_x,start_y]])
visit = [[0 for _ in range(M)] for _ in range(N)]
visit[start_x][start_y] = 1

result = 0
while queue:
  x,y = queue.popleft()
  if input_list[x][y] == "X": continue
  if input_list[x][y] == "P": result += 1
  for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
      if x+dx < 0 or x+dx >= N or y+dy < 0 or y+dy >= M:
        continue
      if visit[x+dx][y+dy]: continue
      visit[x+dx][y+dy] = 1
      queue.append([x+dx, y+dy])

if not result:
  print("TT")
else:
  print(result)