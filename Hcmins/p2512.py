# 입력
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
answer = 0
left, right = 0, max(arr)
# mid을 예측답이라고 하고 이 예측답으로 계산해서 총예산이 넘어가면 상한가를 줄이고 안넘어가면 늘리고 반복

while left <= right:
    mid = (left+right)//2
    sum = 0
    # 예상답에 대한 총예산 계산 (sum : 예상 총예산)
    for i in range(N):
        if (arr[i] > mid):
            sum += mid
        else:
            sum += arr[i]
    # 예상 상한가를 줄이기
    if sum > M:
        right = mid-1
    else:
        left = mid+1
        answer = mid

# 답 출력
print(answer)
