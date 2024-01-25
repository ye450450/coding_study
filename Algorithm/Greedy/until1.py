# 1이 될 때까지
N, K = map(int, input().split())

result = 0

while N != 1:
    rest = N % K
    if rest != 0: 
        result += rest
        N -= rest
    N = N/K
    result += 1

print(result)

# 2번째 방법
# while True:
#     target = (N // K) * K
#     result += (n-target)
#     N = target
    
#     if N < K :
#         break
#     result += 1
#     N //= K
    
# result += (N-1)
# print(result)