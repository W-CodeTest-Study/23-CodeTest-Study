# heapq를 사용해야지 효율성이 통과되는 것 같아서
# 다른 사람 코드 참고하여 이해함.
import heapq

def solution(scoville, K):
  heapq.heapify(scoville)

  answer = 0
  if scoville[0] >= K:
    return answer

  while scoville[0] < K:
    if len(scoville) == 1:
      return -1

    min_scoville = heapq.heappop(scoville)
    min2_scoville = heapq.heappop(scoville)

    heapq.heappush(scoville, min_scoville + min2_scoville*2)
    answer += 1

  return answer

# 정확도 100
# 효율성 0
# heapq 안써서 그런가??
# def solution(scoville, K):
#     answer = 0
#     flag = True

#     while(flag):
#         # 요소가 한개 남은 경우 K이상 못만듬
#         if len(scoville) == 1:
#             break

#         f = True

#         # 오름차순 정렬
#         scoville.sort(reverse=True)

#         # scoville array에 K보다 작은 스코빌 지수가 하나라도 있으면 while문을 계속함
#         for scov in scoville:
#             if scov < K:
#                 f = False
#                 break

#         # f가 True이면 모든 스코빌이 K 이상인 것
#         if f:
#             break

#         # (1,2)번째로 작은 값을 가져와서 새로운 스코빌 지수 생성
#         minScov = []
#         minScov.append(scoville.pop())
#         minScov.append(scoville.pop())

#         newScov = minScov[0] + (minScov[1] * 2)
#         scoville.append(newScov)
#         answer += 1

#     return answer if scoville[0] >= K else -1
