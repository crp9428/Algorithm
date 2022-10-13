import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

a, b, c = map(int, input().strip().split())
print("%d" % (-1 if c <= b else (int(a / (c - b)) + 1 if a % (c - b) == 0 else int(math.ceil(a / (c - b))))))