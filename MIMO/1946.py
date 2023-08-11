import sys

T = int(input())
answer = [] 
for i in range(T):
    N = int(input())
    cnt = 1
    apply = []
    for j in range(N):
        a,b = list(map(int,sys.stdin.readline().split()))
        apply.append([a,b])
    apply = sorted(apply,key = lambda x: x[0])
    tmp = apply[0][1]
    for p in range(1,len(apply)):
        if tmp > apply[p][1]:
            tmp = apply[p][1]
            cnt +=1
    print(cnt)