# 큰 수의 법칙
N , M = map(int, input().split())

result = 0

for i in range(N):
    data = list(map(int, input().split()))
    data.sort() # min(data)
    result = max(data[0], result)
    
print(result)