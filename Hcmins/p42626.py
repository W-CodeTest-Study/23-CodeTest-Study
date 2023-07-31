import heapq


def solution(scoville, K):
    # heap자료구조로 변환
    heapq.heapify(scoville)
    count = 0

    while len(scoville) > 1:
        # 최소 뽑아서 K보다 작은지 확인 후 작으면 공식대로 합쳐서 힙에 다시 넣기
        min = heapq.heappop(scoville)
        if min < K:
            min_second = heapq.heappop(scoville)
            heapq.heappush(scoville, min+2*min_second)
            count += 1
        else:
            break
    # 만들수 없을 때 -1 return
    if heapq.heappop(scoville) < K:
        return -1
    # 만들수 있으면 횟수 return
    else:
        return count
