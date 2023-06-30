#문제 접근 : 접근이랄 것도 없이 dfs/bfs 문제이다.

import sys
from collections import deque #bfs에서 사용할 deque 선언
def dfs(v,r): #dfs 함수 방문했는지 확인후 방문하지 않았다면 루트에 추가, 앞에서 부터 방문
    visiteddfs[v] = 1
    r.append(v+1)
    for i in arr[v]:
        if visiteddfs[i] == 0:
            dfs(i,r)
def bfs(v,r): #bfs 함수 방문했는지 확인 후 방문하지 않았다면 루트에 추가
    visitedbfs[v] = 1
    r.append(v+1)
    q = deque()
    for i in arr[v]: #dfs와 다르게 하나의 노드에 연결되어 있는 모든 노드 추가
        q.append(i)
    while(q):
        cnt = q.popleft() #하나씩 빼면서 방문 확인 및 루트에 추가
        if visitedbfs[cnt] == 0:
            r.append(cnt+1)
            visitedbfs[cnt] = 1
            for i in arr[cnt]:
                q.append(i)

N,M,V = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
for j in range(N): #문제에 숫자가 작은 노드부터 방문하기로 되어있으므로 정렬
    arr[j] = sorted(arr[j])
visiteddfs = [0] * N
rootdfs = []
visitedbfs = [0] * N
rootbfs = []
dfs(V-1,rootdfs)
bfs(V-1,rootbfs)
print(*rootdfs)
print(*rootbfs)