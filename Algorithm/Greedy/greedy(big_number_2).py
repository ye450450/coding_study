# 입력받기
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_num = data[-1]
sencond_num = data[-2]

count = int(M /(K+1)) * K
count += M % (K+1)

sum = 0
sum += count * first_num
sum += (M - count ) * sencond_num
print(sum)
