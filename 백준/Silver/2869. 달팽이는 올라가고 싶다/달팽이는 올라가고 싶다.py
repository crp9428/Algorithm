import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

a, b, v = map(int, input().strip().split())
print("%d" % (math.ceil((v - a) / (a - b)) + 1))