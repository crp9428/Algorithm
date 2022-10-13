import sys
input = sys.stdin.readline
print = sys.stdout.write

while(True):
    a, b = map(int, input().strip().split())
    if a == 0 and b == 0:
        break
    print("%d\n" % (a + b))