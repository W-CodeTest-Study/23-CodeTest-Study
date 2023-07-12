# 프로그래머스 - 입국심사 - lv3
# 이분 탐색

def solution(n, times):
    answer = 0

    # 1부터 최악의 경우의 포인트를 지정
    left, right = 1, max(times)*n

    while left < right:
        mid = (left + right) // 2

        people = 0 # 현재 mid에서 입국심사 가능한 수
        for time in times:
            people += mid // time

        if people >= n: # mid에서 n명 이상 처리할 수 있으면, right를 조정
            right = mid
            answer = mid
        else: # mid에서 n명 미만으로 처리할 수 있으면, left를 조정
            left = mid + 1

    return answer