import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import reduce

n, m = map(int, input().strip().split())
s = set(list(input().strip() for _ in range(n)))
check = list(input().strip() for _ in range(m))
result = reduce(lambda acc, cur: acc + 1 if cur in s else acc + 0, check, 0)
print(f"{result}")