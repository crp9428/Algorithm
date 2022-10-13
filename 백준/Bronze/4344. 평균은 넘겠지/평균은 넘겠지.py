import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import reduce

C = int(input().strip())
for _ in range(C):
    n, *arr = map(int, input().strip().split())
    aver = sum(arr) / n
    result = reduce(lambda acc, cur: acc + 1 if cur > aver else acc + 0 , arr, 0) / n * 100
    print(f'{result:.3f}%\n')