import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import reduce

def isAP(n):
    a = n // 100
    b = (n - (a * 100)) // 10
    c = n - a * 100 - b * 10
    return (c - b == b - a) or (a - b == b - c)

N = int(input().strip())
arr = list(False for _ in range(N + 1))
for i in range(1, N + 1):
    if i < 100:
        arr[i] = True
    else:
        arr[i] = isAP(i)

print("%d\n" % reduce(lambda acc, cur: acc + 1 if cur else acc + 0, arr, 0))