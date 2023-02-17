#그래프가 서로 연결되어 있는지 확인하는 유니온 파인드 알고리즘을 알고 있냐 없냐에 따라서 난이도가 갈리는 문제였던 것 같다. 처음에 유니온 파인드의 개념에 대해 몰랐기 때문에 굉장히 오랜 시간이 걸렸다. 

import sys

#Find 함수
def find(x): #부모 노드가 누구인지 반환한다.
    if parent[x] != x:  #본인이 아니라면 
        parent[x] = find(parent[x]) #누가 부모인지 계속 찾아간다
    return parent[x]


def union(x, y): #더 큰 수를 부모노드로 삼으면서 union 연산을 해준다
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
while True:
    m, n = map(int, sys.stdin.readline().split())
    if m==0 and n==0:
        break
    parent = [i for i in range(m)]
    houserarr = []
    cost = 0
    for i in range(n):
        a,b,c = map(int, sys.stdin.readline().split())
        houserarr.append([a,b,c])
    housearr = sorted(houserarr, key = lambda x: x[2]) #MST를 진행해야 하므로 COST값을 기준으로 정렬 해준다
    for i in housearr:
        u,v,w = i
        if find(u) != find(v):
            union(u,v)
        else:
            cost += w
    print(cost)
