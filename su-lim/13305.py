import sys

input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split())) # 도시 사이 거리
oil_price = list(map(int, input().split())) # 도시 마다 기름 값

result = 0;
current = oil_price[0];

for i in range(N-1):

	if current > oil_price[i]:
		current = oil_price[i]

	result += current * distance[i]

print(result)