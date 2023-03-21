#문제 접근 : dfs문제이다. 하지만, 울타리가 쳐져있는 유형의 dfs는 처음이었기 때문에 조금 당황했다. 그래서 처음에는 울타리를 기준으로 dfs를 돌았지만, 그렇게 하면 울타리를 만났을 때의 처리를 해주지 못해 문제가 발생했다. 늑대와 양은 모두 울타리 안에 있기 때문에 늑대와 양을 기준으로 dfs를 돌아주어야겠다 생각하였다
import sys
sys.setrecursionlimit(10**6)

def dfs(n,m,a):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visited[n][m] = 1
    for i in range(4):
        ddx = n + dx[i]
        ddy = m + dy[i]
        if ddx < 0 or ddx >=R or ddy < 0 or ddy >= C:   #범위 벗어가면 continue
            continue
        elif field[ddx][ddy] == "#":    #울타리 만나면 continue
            continue
        elif field[ddx][ddy] == "." and visited[ddx][ddy] == 0: #.은 continue  v, k를 만나면 동물 배열에 추가해주고 dfs돈다
            dfs(ddx,ddy,a)
        elif field[ddx][ddy] == "v" and visited[ddx][ddy] == 0:
            a.append("v")
            dfs(ddx,ddy,a)
        elif field[ddx][ddy] == "k" and visited[ddx][ddy] == 0:
            a.append("k")
            dfs(ddx,ddy,a)

R,C = map(int, sys.stdin.readline().split())
field = [[]for _ in range(R)]
visited = [[0]*C for _ in range(R)]
wolf = 0
sheep = 0
for i in range(R):
    a = list(sys.stdin.readline().split())
    for j in a[0]:
        field[i].append(j)
for i in range(R):
    for j in range(C):
        animal = []
        if field[i][j] == "v" or field[i][j] == "k":
            if visited[i][j] == 0:
                animal.append(field[i][j])  #자기자신을 animal 배열에 추가해 준뒤 dfs
                dfs(i,j,animal)
                v = animal.count('v')   #dfs를 다 돌고 배열에 있는 값들을 비교
                k = animal.count('k')
                if v<k:
                    sheep += k
                else:
                    wolf += v
print(sheep,wolf)