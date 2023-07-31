from itertools import permutations
def solution(k, dungeons):
    route = []
    answer = []
    for i in permutations(dungeons,len(dungeons)):
        route.append(i)
    for j in route:
        tmp = k
        tmpanswer = 0
        for p in j:
            if tmp >= p[0]:
                tmpanswer +=1
                tmp -= p[1]
            else:
                answer.append(tmpanswer)
                break
            answer.append(tmpanswer)
    return max(answer)