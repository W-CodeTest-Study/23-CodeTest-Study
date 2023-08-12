from collections import deque
def solution(n, m, section):
    answer = 0
    q = deque(section)
    while(len(q)!=0):
        a = q.popleft()
        a-=1
        answer +=1
        if len(q) ==0:
            break
        for i in range(m):
            a += 1
            if q[0] == a:
                q.popleft()
                if len(q)==0:
                    break
    return answer