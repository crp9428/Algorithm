from sys import stdin
input = stdin.readline

N = int(input().strip())
stairs = [0] + [int(input().strip()) for _ in range(N)]

result = [0 for _ in range(N + 1)]
result[1] = stairs[1]
if N >= 2: result[2] = max(result[1] + stairs[2], stairs[2])
if N >= 3: result[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, N + 1):
    result[i] = max(result[i-2] + stairs[i], result[i-3] + stairs[i-1] + stairs[i])

print(result[N])