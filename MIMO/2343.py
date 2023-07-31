import sys

N,M = map(int,sys.stdin.readline().split())
lecture = list(map(int, sys.stdin.readline().split()))
start = max(lecture)
end = sum(lecture)
while start < end:
    cnt = []
    bluelay = []
    cntsum = 0
    mid = (start+end) // 2

    for i in range(N):
        if cntsum+lecture[i] <= mid:
            cnt.append(lecture[i])
            cntsum += lecture[i]
        else:
            bluelay.append([cntsum])
            cnt = []
            cntsum =lecture[i]
            cnt.append(lecture[i])
    bluelay.append([cntsum])
    
    if len(bluelay) < M :
        end = mid - 1
    elif len(bluelay) > M:
        start = mid + 1
    elif len(bluelay) == M:
        end = min(int(max(bluelay)[0]),mid)
print(end)
