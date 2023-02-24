#문제 접근 : 문제를 보고 DP임을 확인하여 점화식을 세웠다. 하지만 맨처음에 짰던 식이 어디서 틀렸는지는 모르겠지만 계속 틀렸다고 나와서 결국 DP로 다른 점화식을 세워 문제를 해결했다
import sys
n,m = map(int, sys.stdin.readline().split())
dp = [1] * (n+1)
if n>=m:
    dp[m] = 2
for i in range(m+1, n+1):
    dp[i] = (dp[i-1] + dp[i-m]) % 1000000007
print(dp[n])

# ans = 0
# a = 2
# b = 3
# if m == 1:
#     ans = 2**n
# elif n<m:
#     ans = 1
# elif n == m:
#     ans = 2
# elif n!=2 and n-m ==1:
#     ans = 3
# else:
#     for i in range(2, n-m+1):
#         ans = a+b
#         a = b
#         b = ans
# print(ans%1000000007)

