#문제 접근 : 문제를 읽고 순열조합이 떠올랐지만, 계속 생각을 해보니 순열조합으로 풀 수 있을까라는 생각이 들어 그래프 이론으로 풀 생각을 해봤다. 유니온 파인드를 해서 싸이클이 존재하면 해당 노드들을 조사해서 싸이클에 있는 인덱스들을 추가하는 방식으로 문제를 해결하려 했다

n = int(input())
a = []
parent = [0] * (n+1)    #유니온파인드를 활용하기 위한 parent배열
answer = []
ranswer = []
a.append(0)
for i in range(1,n+1):  #parent 초기화
    parent[i] = i

def find(parent, x):    #find 함수
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):    #union 함수
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):  #배열에 input number append
    number = int(input())
    a.append(number)
for j in range(1,n+1):
    if find(parent,j) == find(parent,a[j]): #parent가 같다는 것은 cycle이 존재한다는 것이기 때문에 따로 해준다
        cnt = []    
        cnt.append(a[j])
        k=a[j]  #싸이클 확인하기 위해 index를 바꿔주기 위한 변수이다
        while(True):    #while문을 돌면서 싸이클이 돌았는지 확인해준다
            if j == a[k]:   #싸이클이 끝나 자기자신으로 인덱싱 되었다면 break해준다
                cnt.append(a[k])
                break
            else:
                cnt.append(a[k])
                k = a[k]
        answer.append(cnt)
    else:  #cycle이 존재하지 않는다면 union함수를 통해 parent를 최신화 해준다
        union(parent,j,a[j])

for i in range(len(answer)):
    for j in range(len(answer[i])):
        ranswer.append(answer[i][j])

ranswer = list(set(ranswer)) #중복 제거 후 문제에 맞게 프린트
ranswer = sorted(ranswer)
print(len(ranswer))
for i in range(len(ranswer)):
    print(ranswer[i])