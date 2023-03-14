#문제 접근 : 문제를 확인하고 그래프 문제이므로 dfs로 풀어야 겠다는 생각을 하였다.
import sys
sys.setrecursionlimit(5000) #런타임 에러 자꾸 나서 setrecursionlimit 지정
def dfs(arrlist,i,visited,count,cntanswer): #dfs를 돌면서 count가 몇 번째인지 확인
    for node in arrlist[i]: #노드 방문
        if visited[i][node] ==0:    #방문하지 않은 노드라면
            visited[i][node] = 1    #visted = 1 설정
            cntanswer.append(count) #굳이 append를 안하고 visited에 숫자 세팅하는 방식도 있었지만 시간초과 안나서 그냥 진행
            dfs(arrlist, node, visited, count,cntanswer)    #해당 노드에서 다시 dfs 실행
a,b = map(int, sys.stdin.readline().split())
arrlist = [[] for _ in range(a+1)]
for i in range(b):
    c, d = map(int,sys.stdin.readline().split())
    arrlist[c].append(d)
visited = [[0]*(a+1) for _ in range(a+1)]
cntanswer= []
for i in range(len(arrlist)):   #전체 리스트를 돌면서 dfs 실행
    count = i
    if len(arrlist[i]) == 0:
        continue
    else:
        dfs(arrlist,i,visited,count,cntanswer)
print(len(list(set(cntanswer))))