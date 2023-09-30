# 입력
N, M = map(int, input().split())    # N : 강의 수, M : 블루레이 수
lecture = list(map(int, input().split()))

# 답을 mid라고 생각하고 강의를 mid에 맞춰서 배분했을 때 블루레이갯수와 M을 비교해서 답을 움직이는 전략
left, right = max(lecture), sum(lecture)
answer = 0

while left <= right:
    mid = (left+right)//2

    count = 0
    sum = 0
    for i in range(N):
        if sum+lecture[i] > mid:
            count += 1
            sum = 0
        sum += lecture[i]
    # 진행중이던 블루레이가 있을 수 있으니
    if sum > 0:
        count += 1
    # 예측한 답이 블루레이가 더 많이 필요하면 답을 더 늘린다.
    if count > M:
        left = mid+1
    else:
        right = mid-1
        answer = mid

print(answer)
