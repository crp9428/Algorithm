from sys import stdin
input = stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
elements = list(map(lambda x: int(x) - 1, input().strip().split()))
deq = deque([i for i in range(0, N)])
count = 0

while(len(elements) > 0):
    move = -deq.index(elements[0]) if deq.index(elements[0]) < (len(deq) / 2) else (len(deq) - deq.index(elements[0]))
    deq.rotate(move)
    count += abs(move)
    deq.popleft()
    elements = elements[1:]
print(count)