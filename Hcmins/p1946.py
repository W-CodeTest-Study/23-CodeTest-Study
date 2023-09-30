# T = int(input())
# N = []
# all_rank = []
# start_point = 0
# for i in range(T):
#     num = int(input())
#     N.append(num)
#     for j in range(num):
#         all_rank.append(list(map(int, input().split())))
# def check(start_point, num): # 시작포인트랑 몇개까지인지
#     answer = num
#     rank = all_rank[start_point:start_point+num]
#     rank.sort()  # 정렬해서 서류결과비교는 스킵
#     for i in range(num):
#         opt = 0
#         one = rank[i]  # 탈락인지 아닌지 확인할 대상
#         for j in range(i):
#             # 앞에 애들과 면접서류 비교하고 작은게 있으면 opt=1로 바꿈(탈락자라는 의미)
#             if (rank[j][1] < one[1]):
#                 opt = 1
#                 break
#         if (opt == 1):
#             answer -= 1  # 탈락할때마다 전체인원에서 뺌
#     return answer
# for i in range(T):
#     print(check(start_point, N[i]))
#     start_point += N[i]


# 방법2: 반복문 돌리면서 최고순위 임시변수에 저장해두고, but 시간초과
# T = int(input())
# N = []
# all_rank = []
# start_point = 0
# for i in range(T):
#     num = int(input())
#     N.append(num)
#     for j in range(num):
#         all_rank.append(list(map(int, input().split())))
# def check(start_point, num) -> int:
#     answer = 1
#     rank = all_rank[start_point:start_point+num]
#     rank.sort()  # 정렬해서 서류결과비교는 스킵
#     temp = int(rank[0][1])
#     for i in range(1, num):
#         one = rank[i]  # 탈락인지 아닌지 확인할 대상
#         if one[1] < temp:
#             answer += 1
#             temp = one[1]
#     return answer
# for i in range(T):
#     print(check(start_point, N[i]))
#     start_point += N[i]

# 방법3 : 여러가지 필요없는것들 제외하고 깔끔하게 바꾸기
T = int(input())
answer = []
for i in range(T):
    rank = []
    num = int(input())
    for j in range(num):
        rank.append(list(map(int, input().split())))
    rank.sort(key=lambda x: x[0])
    count = 1
    temp = rank[0][1]
    for j in range(1, num):
        if rank[j][1] < temp:
            count += 1
            temp = rank[j][1]
    answer.append(count)
for i in range(T):
    print(answer[i])
