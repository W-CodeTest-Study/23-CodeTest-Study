#문제 접근 : 문제를 읽고 DP인지, greedy인지 고민을 많이 하였다. 하지만, 최댓값만 가지고 계산이 안된다는 결론을 내려 DP로 풀어야 겠다는 생각을 헀다. DP배열에 모든 시간을 넣을 생각을 못했어서 시간이 좀 걸렸지만, 모든 시간을 DP에 넣고 비교해 가며 DP배열을 최신화 해야겠다고 생각하니 문제를 해결할 수 있었다
import sys

N,T = map(int, sys.stdin.readline().split())
times = []
scores = []
dp = [[0 for _ in range(T+1)] for _ in range(N+1)]  #DP배열 생성, 각 초마다 생성
for i in range(N):  
    t,s = map(int,sys.stdin.readline().split()) #따로 저장
    scores.append(s)
    times.append(t)
for i in range(1,N+1):  #단원갯수만큼 돌기
    for j in range(1,T+1):  #시간만큼 돌기
        if j >=times[i-1]:  #j가 times[i-1]보다 크다면, 해당 단원을 공부할 시간이 있는 것이기 때문에 DP비교
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-times[i-1]] + scores[i-1]) #이전 DP와 더하기 전 DP + score를 한 값중 큰 값을 DP로 설정
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][T])