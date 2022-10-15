import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
visit = [False] * N
arr = [0] * M

def dfs(n, depth):
    if depth == M:
        for v in arr:
            print(v, end=" ")
        print()
        return
    
    for i in range(n, N + 1):
        if visit[i - 1]: continue
        visit[i - 1] = True
        arr[depth] = i
        dfs(i, depth + 1)
        visit[i - 1] = False

dfs(1, 0)
        