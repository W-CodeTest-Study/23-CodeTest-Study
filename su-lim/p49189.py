from collections import deque
import sys

def solution(n, edge):

  answer = 0
  MAX = sys.maxsize
  visit = [0]*(n+1)
  weight = [MAX]*(n+1)

  graph = [[] for _ in range(n+1)]
  for [v, u] in edge:
    graph[v].append(u)
    graph[u].append(v)


  q = deque()
  q.append((1, 0))
  while q:
    node, count = q.popleft()
    if visit[node] == 1: continue
    visit[node] = 1
    weight[node] = min(weight[node],count)
    for e in graph[node]:
        q.append((e,count+1))


  answer = weight.count(max(weight[1:]))

  return answer