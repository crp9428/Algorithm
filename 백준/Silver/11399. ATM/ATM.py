import sys
from time import time
input = sys.stdin.readline

N = int(input().strip())
P = list(map(int, input().strip().split()))

P.sort()
times = [P[0]]
for i in range(1, N):
    times.append(times[i - 1] + P[i])

print(sum(times))