import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().strip().split())
cases = list(list(0 for _ in range(11)) for _ in range(11))
cases[0][0], cases[0][1], cases[1][0], cases[1][1] = 1, 1, 1, 1
for i in range(2, N+1):
    for j in range(0, K+1):
        if j == 0 or i == j:
            cases[i][j] = 1
        else:
            cases[i][j] = cases[i-1][j] + cases[i-1][j-1]
print("%d" % cases[N][K])