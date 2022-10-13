import sys
input = sys.stdin.readline
print = sys.stdout.write

n, x = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
for i, v in enumerate(arr):
    if v < x:
        print('%s ' % v)