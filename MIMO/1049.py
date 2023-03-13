#접근 방법 : 문제를 읽으면서 브랜드마다 줄의 길이를 왜 주었는지에 대한 생각을 해보았다. 6줄에 대한 가격과 낱개에 대한 가격을 비교해서 그리디로 풀으면 문제를 해결할 수 있을 것이라 생각하여 여러개의 배열들 중에서 최소 가격에 대한 것만 비교하여 그리디로 풀기로 하였다.
import sys

N,M = map(int, sys.stdin.readline().split())
all = []
one = []
money = 0
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    all.append(a)
    one.append(b)
all = sorted(all)
one = sorted(one)   #배열 정렬 후  첫 번째 인덱스만 사용

while(N!=0):    #N이 다 떨어질때까지 while문
    if N <=6:   #N이 6보다 작으면 낱개 * N을 해서 6개의 가격과 비교
        if all[0] < one[0] * N:
            money+=all[0]
        else:
            money += one[0] * N
        N = 0   #N=0으로 초기화 
    else:   #N이 6보다 크면 6줄의 최소 가격과 낱개 최소 가격*6을 비교
        if all[0] < one[0] * 6:
            money += all[0]
        else:
            money += one[0] * 6
        N -= 6

print(money)