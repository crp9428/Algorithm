# 요세푸스 문제 0
from sys import stdin
input = stdin.readline
from collections import deque

N, K = map(int, input().strip().split())
deq = deque([str(i) for i in range(1, N + 1)])
result = []

while(len(deq) > 0):
    deq.rotate(-K + 1)
    result.append(deq.popleft())
    
print("<" + ", ".join(result).rstrip() + ">")