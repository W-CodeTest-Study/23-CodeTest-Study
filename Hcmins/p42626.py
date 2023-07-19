import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        if len(scoville) < 2:
            break
        min = heapq.heappop(scoville)
        if min < K:
            min_second = heapq.heappop(scoville)
            heapq.heappush(scoville, min+2*min_second)
            count += 1
        else:
            break
    if heapq.heappop(scoville) < K:
        return -1
    else:
        return count
