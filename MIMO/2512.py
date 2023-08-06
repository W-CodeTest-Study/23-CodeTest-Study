import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
M = int(input())
a = sorted(a)
answer = []
start = a[0]
end = a[-1]
while(start <= end):
    mid = (start + end) // 2
    tmp = 0
    for i in range(len(a)):
        if a[i] <= mid:
            tmp += a[i]
        else:
            tmp += mid
    if tmp > M:
        end = mid - 1
    else:
        answer.append(mid)
        start = mid + 1
if len(answer) == 0:
    print(M//n)
else:
    print(max(answer))
