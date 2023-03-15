import sys
from collections import deque
input = sys.stdin.readline

# N: 노드 수, M: 입력 줄 수,  V: 시작 정점 번호
N, M, V = map(int, input().split())

# 양방향 그래프 저장
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 노드 수가 낮은 순으로 접근해야 하므로 정렬
single_node = 0 # 연결된 링크가 없는 단일 노드 수
for link in graph[1:]:
    link.sort()

# DFS - 재귀 사용
result_dfs = []
def dfs(v):
    result_dfs.append(str(v))
    for node in graph[v]:
        if not str(node) in result_dfs: # 방문한 적이 없으면
            dfs(node)

dfs(V)

# BFS - 큐 사용
result_bfs = []
q = deque([V])
while q:
    current = q.popleft()
    if str(current) in result_bfs:
        continue
    result_bfs.append(str(current))

    for node in graph[current]:
        q.append(node)

# 출력
print(" ".join(result_dfs))
print(" ".join(result_bfs))