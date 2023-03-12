#문제 접근 : 처음에는 위상 정렬과 관련된 문제인 줄 알고 굉장히 헤맸다. 하지만, 문제를 꼼꼼히 읽었어야 했다. 순서대로 적혀있는 것을 발견하고 점화식을 세워 DP로 접근했어야 했는데, 그러지 못한 점이 아쉽다.

import sys
n = int(input())
dp = [0] * (n+1)
for i in range(1,n+1):
    work = list(map(int, sys.stdin.readline().split()))
    for j in work[1:]:
        dp[i] = max(dp[i], dp[j] + work[0]) #선행 작업이 순서대로 배치되어 있기 때문에 선행된 작업이 끝난 시간을 기준으로 dp를 해주면 된다
print(max(dp))