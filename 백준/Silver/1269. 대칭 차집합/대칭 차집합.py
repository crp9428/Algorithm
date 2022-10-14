import sys
input = sys.stdin.readline
print = sys.stdout.write

lenA, lenB = map(int, input().strip().split())
A = set(list(map(int, input().strip().split())))
B = set(list(map(int, input().strip().split())))
print("%d" % len(A^B))