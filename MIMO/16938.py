#문제 접근 : 문제를 읽고 조합을 통해 모든 경우의 수를 검증해 나가면서 풀어주어야 겠다 생각했다.
import sys
from itertools import combinations
N,L,R,X = map(int,sys.stdin.readline().split())
problem = []
a = list(map(int,sys.stdin.readline().split()))
problem.append(a)
test = []   #조합으로 얻은 경우의 수를 저장할 배열
answer = 0
for i in range(2,N+1):  #2개 이상의 문제를 넣어야 했으니 조합을 2부터 시작해준다.
    for j in combinations(a,i):
        test.append(j)  #combination으로 얻은 경우의 수를 test에 append
for i in test:
    sumcondition = sum(i)   #모든 문제 난이도 합을 검증하기 위한 변수
    levelcondition = max(i) - min(i)    #문제 최대 난이도와 최소 난이도 차이를 검증하기 위한 변수
    if L<=sumcondition<=R and X<=levelcondition:    #조건에 들어올 경우 +1
        answer+=1
print(answer)
