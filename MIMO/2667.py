#문제 접근 : 전형적인 DFS문제이다. dfs로 이차원 리스트를 돌면서 같은 단지가 몇개인지 세주면 되는 문제이다. 단지를 세주는 방법이 여러가지가 있지만, 효율적으로 구현하기 위해서 딕셔너리를 사용하여 같은 단지가 나올때마다 하나씩 더해주는 방식으로 구현해 주었다
import sys
def dfs(a,b):   #dfs 함수, 같은 단지이면 answer[count] += 1을 해주었다
    visited[a][b] = 1
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    for i in range(4):
        ddx = a + dx[i]
        ddy = b + dy[i]
        if ddx < 0 or ddx >=n  or ddy < 0 or ddy >= n:
            continue
        elif house[ddx][ddy] == '1' and visited[ddx][ddy] == -1:
            answer[count] += 1
            dfs(ddx,ddy)


n = int(input())
house = []
count = 0
for i in range(n):
    cntarr = []
    a = list(sys.stdin.readline().split())
    for j in range(len(a[0])):  #숫자 하나씩 배열로 저장해주기 위해서 for문을 돌면서 하나씩 append 해주었다
        cntarr.append(a[0][j])
    house.append(cntarr)
visited = [[-1]*n for _ in range(n)]
answer = {} #단지 개수 저장해주기 위해서 딕셔너리로 선언
for i in range(n):
    for j in range(n):
        if house[i][j] == '1' and visited[i][j] == -1:  #1이면서 방문하지 않았던 곳이라면 dfs함수 돌기
            count += 1
            answer[count] = 1   #맨 처음 발견한 것은 count가 안되기 때문에 애초에 1로 시작한다
            dfs(i,j)
answer = list(answer.items())
realanswer = []
for i in range(len(answer)):    #정렬하기 위해 하나의 배열에 추가해준다
    realanswer.append(answer[i][1])
realanswer = sorted(realanswer)
print(len(realanswer))
for i in realanswer:
    print(i)