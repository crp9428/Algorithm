import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().strip().split())
comb = list(list(-1 for i in range(j+1)) for j in range(N+1))
comb[0][0], comb[1][0], comb[1][1] = 1, 1, 1

for i in range(2, N+1):
    for j in range(0, i+1):
        if j == 0 or j == i:
            comb[i][j] = 1
        else:
            comb[i][j] = comb[i-1][j] + comb[i-1][j-1]

print("%d\n" % (comb[N][K] % 10007))