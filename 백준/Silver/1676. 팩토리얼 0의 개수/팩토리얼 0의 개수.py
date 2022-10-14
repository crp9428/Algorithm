import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
print("%d" % (N // 5 + N // 25 + N // 125))