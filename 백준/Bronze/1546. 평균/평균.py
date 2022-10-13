import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
arr = list(map(int, input().strip().split()))
M = max(arr)
new = list(map(lambda x: x / M * 100, arr))
print("%f\n" % (sum(new) / len(new)))