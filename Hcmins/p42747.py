def solution(citations):
    citations.sort()
    maxs = [0]
    # 결국 0 부터 +1 되면서 최대크기까지 돌음
    # h가 사이에 있을땐 그것보다 작은 값인 citations[i]에 종속되서 more,less를 구함
    for i in range(len(citations)):
        if i == 0:
            min = 0
        else:
            min = citations[i-1]+1

        for h in range(min, citations[i]+1):
            # h가 citations에 있으면 그 값까지 이하에 포함이라 less+1 해줘야됨
            if h == citations[i]:
                less = i+1
            else:
                less = i
            more = len(citations)-i
            # h조건에 부합하는거 다 저장 후 그 중 최대값이 return값
            if h <= more and h >= less:
                maxs.append(h)
    answer = max(maxs)
    return answer
