import sys
input = sys.stdin.readline
print = sys.stdout.write
import math

N = int(input().strip())
ii = math.floor(math.sqrt(N)) + 1
arr = []
for i in range(2, ii):
    while(True):
        if N % i == 0:
            arr.append(i)
            N = int(N / i)
        else:
            break
if N != 1:
    arr.append(N)
    
for v in arr:
    print("%d\n" % v)