from sys import stdin
input = stdin.readline

N = int(input().strip())
triangle = list(list(map(int, input().strip().split())) for _ in range(N))

for i in range(1, N):
    for j, v in enumerate(triangle[i]):
        lastIdx = len(triangle[i]) - 1
        if j == 0:
            triangle[i][j] += triangle[i-1][0]
        elif j == lastIdx:
            triangle[i][j] += triangle[i-1][lastIdx-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
            
print(max(triangle[N - 1]))