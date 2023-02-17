#문제 접근 : 문제 이해하는게 오래 걸리고, 시간 초과 때문에 애를 좀 먹었다. 처음에는 첫날 부터 마지막 날까지 쭈욱 애벌레를 증가시켰는데, 그 부분에서 시간을 많이 잡아 먹어서 한번에 더하는 형식으로 바꾸어 주었다. 

import sys

M, N = map(int, sys.stdin.readline().split())

bee = [[1]*M for _ in range(M)] #벌집 배열 생성
grow = []
growarray = [0]*(2*M-1) #맨왼쪽 아래부터 맨 위 오른쪽까지 수만큼 배열 생성
for i in range(N): 
    a,b,c = map(int, sys.stdin.readline().split())
    for w in range(a, a+b): #0은 안더해줘도 되니, 1의 갯수만큼 돌면서 1을 더해준다.
        growarray[w] += 1
    for w in range(a+b, 2*M-1): #2도 마찬가지
        growarray[w] += 2

for j in range(M-1,-1,-1):  #적어둔 growarray를 바탕으로 bee 배열을 업데이트 한다.
    bee[j][0] += growarray[(M-1)-j]
for l in range(1, M):
    bee[0][l] += growarray[l+(M-1)]

for x in range(1,M):
    for y in range(1,M):    #max로 하면 시간 초과가 나서 어떻게 할까 고민하다가 어짜피 맨 위를 비교해서 갱신하기 때문에 처음부터 맨 위를 비교해주는 방식으로 변경하였다.
        bee[x][y] += bee[0][y] - 1
for i in bee:
    print(*i)
