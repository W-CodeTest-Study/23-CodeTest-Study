import sys

n = int(input())
far = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))
answer = 0
now = city[0]   #now 첫번째 도시로 초기화 
i = 0
while(True):    #모든 도시 돌기 
    if now > city[i]:   #만약 다음 도시가 now보다 작다면
        now = city[i]   #now 초기화
    answer += far[i] * now  #now값을 기준으로 기름값을 계산해준다
    i+=1    #다음 도시로~
    if i == len(far):   #마지막 도시는 검사할 필요 없으므로 종료
        break
print(answer)