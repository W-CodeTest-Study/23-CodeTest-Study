a = input()
b = input()
answer = 0
if len(a) > len(b):
    a,b = b,a
dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i+1][j+1] = dp[i][j]+ 1
            if answer < dp[i+1][j+1]:
                answer = dp[i+1][j+1]
print(answer)