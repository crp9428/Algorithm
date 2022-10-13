import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
print("%d" % (math.ceil((3 + math.sqrt(-3 + 12*n)) / 6)))