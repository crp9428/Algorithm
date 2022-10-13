import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input().strip())
for i in range(t): 
    h, w, n = map(int, input().strip().split())
    yy = h if n % h == 0 else n % h
    xx = n // h if n % h == 0 else n // h + 1
    result = str(yy) + str(xx).zfill(2)
    print("%s\n" % result)