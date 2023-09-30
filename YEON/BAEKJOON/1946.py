import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())

    ranks = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    ranks.sort() # 서류 성적순으로 정렬

    min_rank = ranks[0][1]

    cnt = 1

    for i in range(n):
        rank = ranks[i][1]
        # 서류 성적 높은애보다 면접 성적이 더 좋아야함.
        if rank < min_rank:
            min_rank = rank
            cnt += 1

    print(cnt)
