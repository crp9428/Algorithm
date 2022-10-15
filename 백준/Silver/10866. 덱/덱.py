from sys import stdin
input = stdin.readline
from collections import deque

N = int(input().strip())
deq = deque()
for _ in range(N):
    cmd = list(input().strip().split())
    if cmd[0] == "push_front":
        x = int(cmd[1])
        deq.appendleft(x)
    elif cmd[0] == "push_back":
        x = int(cmd[1])
        deq.append(x)
    elif cmd[0] == "pop_front":
        print(deq.popleft()) if len(deq) > 0 else print(-1)
    elif cmd[0] == "pop_back":
        print(deq.pop()) if len(deq) > 0 else print(-1)
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        print(0) if len(deq) > 0 else print(1)
    elif cmd[0] == "front":
        print(deq[0]) if len(deq) > 0 else print(-1)
    elif cmd[0] == "back":
        print(deq[-1]) if len(deq) > 0 else print(-1)