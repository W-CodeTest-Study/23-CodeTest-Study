#문제 접근 : 전형적인 bfs문제다 visited에 방문했다는 것을 나타내는 것이 아니라 거리를 적어주면 쉽게 bfs로 훑으면서 해결해줄 수 있는 문제다
from collections import deque
def solution(n, vertex):
    visited = [-1] * (n+1) #visited 배열 초기화
    node = [[] for _ in range(n+1)] #bfs하기 쉽게 인덱스별로 요소를 받아줄 배열을 선언해준다
    far = 1 #처음 거리는 1로 설정
    answer = 0
    q = deque() #popleft를 하며 꺼내줄 거기 때문에 deque로 선언(사실 큐에 하나씩만 들어가기 때문에 그냥 배열로 선언하고 pop했어도 상관없었을듯)
    for i in range(len(vertex)): #vertex를 돌며 방문 노드를 추가
        node[vertex[i][0]].append(vertex[i][1])
        node[vertex[i][1]].append(vertex[i][0])
    q.append(node[1]) #큐에 가장 1번 노드와 연결되어 있는 요소들을 추가해준다 
    visited[1] = 0 #1번에 있는 요소들을 빼줬으므로 방문 처리 해준다
    while q: #큐가 빌때까지 돌기
        far +=1 #한번 돌 때마다 거리가 1씩 증가한다
        cnt = q.popleft() 
        cntarr = [] #q에 한번에 append해주기위해 임시 배열 설정
        for i in range(len(cnt)): #꺼내준 노드에 연결된 노드만큼 for문을 돌면서
            if visited[cnt[i]] == -1: #들르지 않았다면
                visited[cnt[i]] = far #해당 요소를 far만큼 업데이트 해준다
                for j in range(len(node[cnt[i]])): #그리고 나서 그 해당 노드와 연결되어 있는 노드들의 갯수만큼 for문을 돌면서
                    if visited[node[cnt[i]][j]] == -1: #방문하지 않았다면
                        cntarr.append(node[cnt[i]][j]) #이후에 방문해야 하기 때문에 cntarr에 append해준다
        if len(cntarr) == 0: #cntarr가 없다면 종료
            break
        q.append(cntarr) #있다면 append
    maxlength = max(visited) #최댓값 계산
    for i in visited:
        if maxlength == i:
            answer+=1
    return answer