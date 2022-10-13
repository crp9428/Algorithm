import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import reduce

X = int(input())
N = int(input())
items = list(list(map(int, input().strip().split())) for _ in range(N))
total = reduce(lambda acc, cur: acc + cur[0]*cur[1], items, 0)
print('Yes') if X == total else print('No')