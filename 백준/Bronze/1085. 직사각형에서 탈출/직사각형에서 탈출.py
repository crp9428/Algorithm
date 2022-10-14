import sys
input = sys.stdin.readline
print = sys.stdout.write

x, y, w, h = map(int, input().strip().split())
print("%d" % (min(h-y, y-0, w-x, x-0)))