# 큐 2
import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N = int(input().strip())
deq = deque()
for _ in range(N):
    cmd = list(input().strip().split())
    if cmd[0] == 'push':
        x = int(cmd[1])
        deq.append(x)
    elif cmd[0] == 'pop':
        print("%s\n" % deq.popleft()) if len(deq) > 0 else print("-1\n")
    elif cmd[0] == 'size':
        print("%d\n" % len(deq))
    elif cmd[0] == 'empty':
        print("1\n") if len(deq) == 0 else print("0\n")
    elif cmd[0] == 'front':
        print("%s\n" % deq[0]) if len(deq) > 0 else print("-1\n")
    elif cmd[0] == 'back':
        print("%s\n" % deq[-1]) if len(deq) > 0 else print("-1\n")
