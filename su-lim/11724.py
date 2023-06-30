# 백준 11724
# 연결 요소의 개수를 구하는 문제
# 문제 접근 : BFS를 이용하여 해결
import sys
from collections import deque
input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

# 연결 요소의 개수 구하기
count = 0
visit = [0] * (N+1)

def BFS(v):
  q = deque([v])
  while q:
    current = q.popleft()
    if visit[current] == 1: continue # (1)
    visit[current] = 1

    for node in graph[current]: # (2)
        q.append(node)
    # (2)자리에 (1) 코드를 두면 시간초과남
    # q에 집어넣을 때 visit을 확인하는 것 (2)
    # 일단 넣고 q에서 pop한 후 바로 확인하는 것 (1)
    # 시간 차이가 없을 것 같았는데 왜 다르죵?

for i in range(1,N+1):
  if visit[i] == 0:
    count += 1
    BFS(i)

# 정답 출력
print(count)