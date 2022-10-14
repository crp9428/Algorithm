import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input().strip())
comb = list(list(-1 for i in range(j+1)) for j in range(31))
comb[0][0], comb[1][0], comb[1][1] = 1, 1, 1

for _ in range(T):
    N, M = map(int, input().strip().split())
    if N == 1:
        print("%d\n" % M)
    elif N == M:
        print("1\n")
    elif comb[M][N] == -1:
        for i in range(2, M+1):
            for j in range(0, i+1):
                if j == 0 or j == i:
                    comb[i][j] = 1
                else:
                    comb[i][j] = comb[i-1][j] + comb[i-1][j-1]
        print("%d\n" % comb[M][N])
    else:
        print("%d\n" % comb[M][N])