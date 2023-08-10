# 메모리 추가 ㅠ
from itertools import permutations
N = input()

arr = list(map(int, str(N)))

arr.sort(key=lambda x: -x)
# 30의 배수가 아닌 조건 확인
if arr[len(arr)-1] != 0 or sum(arr) % 3 != 0:
    print(-1)
# 3의 배수를 만들 수 있는데 그 값을 찾기
else:
    arr.remove(0)
    permute = list(permutations(arr))
    for i in range(len(permute)):
        num = ''.join(map(str, list(permute[i])))
        if int(num) % 3 == 0:
            print(num+'0')
            break
