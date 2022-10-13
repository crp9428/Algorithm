import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import reduce

t = int(input().strip())
for _ in range(t):
    r, s = map(lambda x: int(x) if x.isdigit() else x, input().strip().split())
    result = reduce(lambda acc, cur: acc + cur*r, s, "")
    print("%s\n" % result)