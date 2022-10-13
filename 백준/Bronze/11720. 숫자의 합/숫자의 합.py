import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
num = list(map(int, input().strip()))
print("%d" % sum(num))