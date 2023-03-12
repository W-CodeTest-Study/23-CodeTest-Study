#문제 접근 : BFS로 경로를 계산하면 되는 문제였는데 자료구조를 dict로 가져가다가 자꾸 key error가 나서 결국 인터넷의 도움을 받았다.
import sys
import collections


n = int(input())
q = collections.deque()
friend = [[] for _ in range(n+1)]
route = [[0]*(n+1) for _ in range(n+1)]
cntmax = []
man = []
while(True):
    a,b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    else:
        friend[a].append(b) #딕셔너리가 아닌 배열로 계산해주기 위해 배열에 추가를 해준다
        friend[b].append(a)
def bfs(i,n):   #bfs로 경로를 돌면서 추가를 해준다
    visited[n] = True
    q.append(n)
    while q:
        x = q.popleft()
        for j in friend[x]:
            if not visited[j]:
                q.append(j)
                route[i][j] = route[i][x] + 1   #이전 경로에서 하나 더왔으니 이렇게 값을 넣어준다..
                visited[j] = True

for i in range(n):
    visited = [False] * (n+1)
    bfs(i+1,i+1)
for p in range(n+1):    #위에서 bfs를 i 순으로 돌아주었기 때문에 반대편 경로도 동기화 해주기 위해 for문을 돌아준다
    for q in range (n+1):
        if route[p][q] !=0:
            if route[q][p] == 0:
                route[q][p] = route[p][q]
            else:
                route[q][p] = min(route[p][q], route[q][p])
                route[p][q] = route[q][p]
for i in range(1,n+1):
    a = max(route[i])
    cntmax.append(a)
cntmax = sorted(cntmax)
for i in range(1, n+1):
    if max(route[i]) == cntmax[0]:
        man.append(i)
man = sorted(man)
print("{} {}".format(cntmax[0],len(man)))
print(*man)
    