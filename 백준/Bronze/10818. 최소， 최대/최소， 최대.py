import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
nums = list(map(int, input().strip().split()))
print("%d %d\n" % (min(nums), max(nums)))