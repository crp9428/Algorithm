import sys
input = sys.stdin.readline

N = int(input().strip())
stairs = [[0 for _ in range(10)] for _ in range(N + 1)]
for i in range(1, 10):
    stairs[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            stairs[i][0] = stairs[i - 1][1]
        elif j == 9:
            stairs[i][9] = stairs[i - 1][8]
        else:
            stairs[i][j] = stairs[i - 1][j - 1] + stairs[i - 1][j + 1]

print(sum(stairs[N]) % 1000000000)