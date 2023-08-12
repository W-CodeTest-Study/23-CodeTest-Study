# 방법1: 테케 3개 시간초과
# def solution(n, m, section):
#     answer = 0
#     maxinum = section[0]
#     while maxinum <= max(section):
#         maxinum += m
#         answer += 1
#         for num_section in section:
#             if (maxinum <= num_section):
#                 maxinum = num_section
#                 break
#     return answer

# 방법1 향상된 버전 : 여전히 3개 시간초과
def solution(n, m, section):
    answer = 0
    maxinum = section[0]
    index = 0
    while maxinum <= max(section):
        maxinum += m
        answer += 1
        for i in range(index, len(section)):
            if (maxinum <= section[i]):
                maxinum = section[i]
                break
            index = i
    return answer


# 방법2 : binary_search로 그 maxinum보다 크거나 같은 가장 최소값의 index(mid)을 찾아낸다
def solution(n, m, section):
    answer = 0
    maxinum = section[0]
    index = 0  # 아직 안칠한 곳의 첫번째 index
    while maxinum <= max(section):
        maxinum += m
        answer += 1
        r = len(section)-1
        while index <= r:
            mid = (index+r+1)//2
            if (maxinum > section[mid]):  # 이미 칠한 곳
                index = mid+1
            elif (maxinum <= section[mid] and maxinum <= section[mid-1]):
                r = mid-1
            else:  # 여기에서의 mid이 아직 안칠한곳의 시작지점
                maxinum = section[mid]
                index = mid
                break
    return answer
