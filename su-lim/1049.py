# 백준 1049 - 기타줄
# 문제 접근 : 여러 브랜드의 상품이 제시되더라도,
#           6개 패키지 가격이 가장 저렴한 브랜드의 가격, 1개 가격이 가장 저렴한 브랜드의 가격만으로 결과를 구한다.

# 1. 입력
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

MAX_PRICE = 1000
six_price, one_price = MAX_PRICE, MAX_PRICE
for _ in range(M):
  A, B = map(int, input().split())
  if six_price > A: six_price = A # 6개 패키지 가격이 가장 저렴한 브랜드 가격 저장
  if one_price > B: one_price = B # 1개 가격이 가장 저렴한 브랜드 가격 저장

# 2. 가장 저렴한 경우 계산 후 출력
if six_price > one_price * 6: # 개당 가격이 6개 패키지 보다 저렴하면, 패키지로 구매할 이유가 없으므로
  print(one_price * N)
  exit()

q = int(N/6)
remain = N%6
# 6개 패키지로만 구매하는게 더 저렴한 경우, 6개 패키지로 구매 후 낱개 구매를 하는게 더 저렴한 경우를 계산하여 출력
result = min(q * six_price + (remain and six_price) , q * six_price + (remain * one_price))
print(result)