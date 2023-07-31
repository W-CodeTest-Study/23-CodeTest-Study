def solution(citations):
    citations = sorted(citations)
    answer = min(citations)
    for i in range(len(citations)+1):
        for j in range(len(citations)-1):
            if citations[j] <= i and citations[j+1] >= i:
                upper = len(citations) - (j+1)
                if upper >= i:
                    answer = i
    if answer > len(citations):
        answer = len(citations)
    return answer