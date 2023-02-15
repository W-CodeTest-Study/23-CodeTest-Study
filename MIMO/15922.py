#문제만 이해하면 아주 쉽게 풀 수 있다. 문제 이해하는게 어려워서 골드 5인것 같다.
import sys
n = int(input())
fun = []
ans = 0
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    if len(fun) == 0:   #첫 입력이라면 그냥 배열에 추가를 해준다.
        fun.append([a,b])
    else:   #두 번째 입력 부터는 이전 입력된 선분에 포함이 되어있는지 검사를 해준다.
        if fun[-1][1] > a:  #포함이 되어 있다면 완전 포함되어 있는지, 한쪽만 포함되어있는지 검사후 추가해준다.
            if fun[-1][1] <b:
                fun[-1][1] = b
        else:
            fun.append([a,b]) #포함되어 있지 않다면 하나 더해준다.
for i in fun:
    c,d = i[0],i[1]
    ans += d-c
print(ans)