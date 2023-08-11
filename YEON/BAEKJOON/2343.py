
N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
left, right = max(arr), sum(arr)
# left: 블루레이 가장 큰값 ex) 9
# right: 블루레이 하나에 들어가는 총 강의의 길이 제일 큰 값은 sum 값 45

while left <= right:
    mid = (left+right) // 2

    count, sum = 0, 0
    for i in range(N):
        if sum + arr[i] > mid:
            count += 1
            sum = 0
        sum += arr[i]
    if sum:
        count += 1

    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)
