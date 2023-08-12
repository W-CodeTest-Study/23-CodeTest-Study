T = int(input())
N = []
all_rank = []
start_point = 0
for i in range(T):
    num = int(input())
    N.append(num)
    for j in range(num):
        all_rank.append(list(map(int, input().split())))

# 시작포인트랑 몇개까지인지


def check(start_point, num):
    answer = num
    rank = all_rank[start_point:start_point+num]
    rank.sort()  # 정렬해서 서류결과비교는 스킵
    for i in range(num):
        opt = 0
        one = rank[i]  # 탈락인지 아닌지 확인할 대상
        for j in range(i):
            # 앞에 애들과 면접서류 비교하고 작은게 있으면 opt=1로 바꿈(탈락자라는 의미)
            if (rank[j][1] < one[1]):
                opt = 1
                break
        if (opt == 1):
            answer -= 1  # 탈락할때마다 전체인원에서 뺌
    return answer


for i in range(T):
    print(check(start_point, N[i]))
    start_point += N[i]
