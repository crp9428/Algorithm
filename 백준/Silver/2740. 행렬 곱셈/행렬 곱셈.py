from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N, M = map(int, input().strip().split())
A = list(list(map(int, input().strip().split())) for _ in range(N))
M, K = map(int, input().strip().split())
B = list(list(map(int, input().strip().split())) for _ in range(M))
result = list(list(0 for _ in range(K)) for _ in range(N))

for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += A[n][m] * B[m][k]

for n in range(N):
    for k in range(K):
        print("%d " % result[n][k])
    print("\n")