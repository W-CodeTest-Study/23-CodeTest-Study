
import sys

num = list(sys.stdin.readline().strip())
# 30의 배수는
# 10의 배수이면서
# 3의 배수
# num에 0이 없으면 -1 리턴

if '0' in num:
    sum = 0
    for n in num:
        sum += int(n)

    if sum % 3 != 0 :
        print(-1)
    else:
        num = sorted(num, reverse=True)
        print("".join(num))

else:
    print(-1)
