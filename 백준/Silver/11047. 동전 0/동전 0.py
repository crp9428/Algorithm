import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
coins = [int(input().strip()) for _ in range(N)]

count = 0
for i in range(N - 1, -1, -1):
    if K == 0: break
    elif coins[i] > K: continue
    count += (K // coins[i])
    K -= ((K // coins[i]) * coins[i])
    
print(count)