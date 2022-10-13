import sys
input = sys.stdin.readline
print = sys.stdout.write

a, b = input().strip().split()
rA = int(a[::-1])
rB = int(b[::-1])
print("%d" % (rA if rA > rB else rB))