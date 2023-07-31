# 프로그래머스 - lv 2 더 맵게 - heap
import heapq

def solution(scoville, K):
	answer = 0;

	heapq.heapify(scoville)

	while(scoville[0] < K):

		if len(scoville) < 2:
			return -1

		min1 = heapq.heappop(scoville) # 가장 낮은 스코빌 지수인 음식
		min2 = heapq.heappop(scoville) # 두번째로 낮은 스코빌 지수인 음식
		heapq.heappush(scoville,  min1 + (min2 * 2) )
		answer += 1

	return answer