# 백준 - 문제집 (위상정렬 문제)
# 문제 접근 : 일반적인 위상정렬 알고리즘에서 착안하여 구현

# 1. 입력 및 초기화
import sys, heapq
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 문제 수, 다음 입력 받을 줄 수
in_degree = [0]* (N+1) # 문제 별 진입 차수 저장
graph = [[] for _ in range(N+1)] # 연결 정보를 저장
visit = [0] * (N+1)
result = []
q = []

for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  in_degree[B] += 1

# 2. 방문하지 않은 진입 차수 0인 점을 큐에 삽입

# 진입차수가 0인 값들 큐에 넣음
for i in range(1,len(in_degree)):
  if in_degree[i] == 0:
    heapq.heappush(q, i)

while len(result) != N:
  if not q: # 만약 q가 비어있다면 방문하지 않은 node중 첫번째를 q에 넣음
    node = visit[1:].index(0)
    heapq.heappush(q, node)
    visit[node]

  current = heapq.heappop(q) # q에 있는 값 중 첫번째를 꺼내어 resuilt에 넣고 방문처리
  result.append(str(current))
  visit[current] = 1

  for node in graph[current]: # current와 연결된 node의 진입차수 제거
    in_degree[node] -= 1
    if in_degree[node] == 0 and visit[node] == 0: # 방문한적 없는 node의 indegree가 0이 되면 q에 넣어둠
      heapq.heappush(q, node)

# 3. 답안 출력
print(" ".join(result))