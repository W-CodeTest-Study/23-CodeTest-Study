from collections import deque

def solution(begin, target, words):
    q = deque()
    if target not in words:
        return 0
    else:
        q.append([begin,0])
        while(q):
            cnt = q.popleft()
            if cnt[0] == target:
                return cnt[1]
                break
            else:
                for i in words:
                    temp = 0
                    for j in range(len(begin)):
                        if i[j] != cnt[0][j]:
                            temp += 1
                    if temp == 1:
                        q.append([i,cnt[1]+1])

