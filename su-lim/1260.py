# 백준 1260
# 문제 접근 : BFS, DFS만 하면 되는 간단한 문제. 정렬을 해야함
# 후기 : BFS는 반복문, DFS는 재귀로 꼭 풀어야겠다

import sys
from collections import deque
input = sys.stdin.readline

# N: 노드 수, M: 입력 줄 수,  V: 시작 정점 번호
N, M, start = map(int, input().split())

# 양방향 그래프 저장
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 노드 수가 낮은 순으로 접근해야 하므로 각 링크를 정렬
for link in graph[1:]:
    link.sort()

# DFS - 재귀 사용
result_dfs = [] # visit와 출력 용도로 사용
def dfs(v):
    result_dfs.append(str(v))
    for node in graph[v]:
        if not str(node) in result_dfs: # 방문한 적이 없으면
            dfs(node)
dfs(start)

# BFS - deque 사용
result_bfs = []
q = deque([start])
while q:
    current = q.popleft()
    if str(current) in result_bfs:
        continue
    result_bfs.append(str(current))

    for node in graph[current]: # 현재 노드와 연결된 모든 노드를 큐에 넣음
        q.append(node)

# 출력
print(" ".join(result_dfs))
print(" ".join(result_bfs))