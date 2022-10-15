import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
visit = [False] * N
arr = [0] * M

def dfs(depth):
    if depth == M:
        for v in arr:
            print(v, end=" ")
        print()
        return
    
    for i in range(N):
        if visit[i]: continue
        visit[i] = True
        arr[depth] = i + 1
        dfs(depth + 1)
        visit[i] = False
        
dfs(0)