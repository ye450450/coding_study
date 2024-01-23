# 입력받기
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
sum = 0
count = 0
for i in range(M):
    if(count != 3):
        sum += data[-1]
        count += 1
    else:
        sum += data[-2]
        count = 0
print(sum)