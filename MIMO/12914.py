def solution(n):
    cnt = [1,2]
    if n == 1 or n == 2:
        return cnt[n-1]
    else:
        for i in range(n-2):
            cnt.append(cnt[i] + cnt[i+1])
    return cnt[n-1] % 1234567