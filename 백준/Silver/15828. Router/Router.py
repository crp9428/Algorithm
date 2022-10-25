from sys import stdin
input = stdin.readline
from collections import deque

N = int(input().strip())
n = int(input().strip())
router = deque()
i = 0

while(n != -1):
    if n == 0:
        router.popleft()
        i -= 1
    elif i < N:
        router.append(n)
        i += 1
        
    n = int(input().strip())

if len(router) == 0:
    print("empty")
else:
    for i in range(0, N):
        try:
            print(router[i], end=' ')
        except IndexError:
            break