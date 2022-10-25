N, M = map(int, input().strip().split())
A = list(list(map(int, input().strip().split())) for _ in range(N))
B = list(list(map(int, input().strip().split())) for _ in range(N))

for n in range(N):
    for m in range(M):
        print(A[n][m] + B[n][m], end=' ')
    print()