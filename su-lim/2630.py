# 백준 - 색종이 만들기
import sys
from collections import deque
input = sys.stdin.readline

# color(): 정사각형이 어떤 색으로 되어있는지 확인, 중간에 다른 색이 있으면 -1
def color(maps):
  default = maps[0][0]
  for row in maps:
    for c in row:
      if c != default:
        return -1
  return default

# div(): 정사각형 배열을 가로세로 크기가 1/2된 배열로 나누는 함수
# [1,1],[2,2] -> [1],[1],[2],[2]
def div(maps):
  l = int(len(maps)/2)
  r1, r2, r3, r4 = maps[:l], maps[:l], maps[l:], maps[l:]

  for i in range(len(r1)):
    r1[i] = r1[i][:l]
    r2[i] = r2[i][l:]
    r3[i] = r3[i][:l]
    r4[i] = r4[i][l:]

  return [r1,r2,r3,r4]

# 입력 처리
N = int(input())
in_maps = []
for i in range(N):
  in_maps.append(list(map(int, input().split())))

result = [0,0]

# 색종이 수 구하기
q = deque([in_maps])
while(q):
  cur_maps = q.popleft()

  # 한 가지 색으로 이루어진 경우 (0, 1)
  if color(cur_maps) == 1 or color(cur_maps) == 0 :
    result[color(cur_maps)] += 1
    continue

  # 한 가지 색으로 이루어지지 않은 경우 (-1)
  div_maps = div(cur_maps)
  for maps in div_maps:
    q.append(maps)

# 결과 출력
print(result[0])
print(result[1])