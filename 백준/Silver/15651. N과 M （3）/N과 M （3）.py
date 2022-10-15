import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
visit = [[False] * N for _ in range(M)]
arr = [0] * M

def dfs(depth):
    if depth == M:
        print(" ".join(str(v) for v in arr))
        return

    for i in range(N):
        if visit[depth][i]: continue
        visit[depth][i] = True
        arr[depth] = i + 1
        dfs(depth + 1)
        visit[depth][i] = False

dfs(0)
