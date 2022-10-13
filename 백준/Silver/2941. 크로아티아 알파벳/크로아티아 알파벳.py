import sys
import re
input = sys.stdin.readline
print = sys.stdout.write

ss = input().strip()
result = re.sub("c=|c-|dz=|d-|lj|nj|s=|z=", "0", ss)
print("%d" % len(result))