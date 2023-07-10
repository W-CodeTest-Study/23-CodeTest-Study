def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for i in times:
            people += mid // i
            if people >=n:
                break
        if people >=n:
            right = mid-1
        else:
            left = mid+1
    return left