import sys
input = sys.stdin.readline
from collections import deque

T = int(input().strip())

for _ in range(T):
    N, M = map(int, input().strip().split())
    docs = deque(map(int, input().strip().split()))
    count = 0
    
    while(M >= 0):
        maxImportance = max(docs); maxIdx = docs.index(maxImportance)
        docs.rotate(-maxIdx)
        M -= maxIdx
        docs.popleft()
        count += 1
        if M == 0:
            break
        else:
            M = M - 1 if M > 0 else M + len(docs)
        
    print(count)
